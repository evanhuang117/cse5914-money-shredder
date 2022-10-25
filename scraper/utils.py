from abc import abstractmethod
import asyncio
import aiohttp
import httpx
from logger import logger
from config import *
from ebay_browse_api_client.ebay_browse_api_client import AuthenticatedClient
from ebay_browse_api_client.ebay_browse_api_client.models.search_paged_collection import SearchPagedCollection
from ebay_browse_api_client.ebay_browse_api_client.api.item_summary import search
from ebay_browse_api_client.ebay_browse_api_client.types import Response
import requests
import base64
import json

"""
interleaves two arrays with the same length, with the first element of arr1 as the first element
"""


async def interleave(arr1, arr2):
    result = arr1 + arr2
    result[::2] = arr1
    result[1::2] = arr2
    return result


class Searcher:
    def __init__(self, session: aiohttp.ClientSession, id_keys: list[str], index_name: str) -> None:
        self.session = session
        self.id_keys = id_keys
        self.index_name = index_name

    async def process_listings(self, listings):
        # create es actions and ids for listings
        actions = [{'update': {'_id': "".join([str(l.get(k)) for k in self.id_keys]),
                               '_index': self.index_name}}
                   for l in listings]
        # replace newline chars in text bc bulk uses new line delimited json
        listings = [{key: value.replace('\n', '') if isinstance(value, str) else value
                    for key, value in l.items()}
                    for l in listings]

        # create docs to upsert
        # add upsert=true to all results
        listings = [{'doc': l, 'doc_as_upsert': 'true'} for l in listings]
        return await interleave(actions, listings)

    async def get_bulk_actions(self):
        async for l in self.get_listings():
            if l:
                yield await self.process_listings(l)

    @abstractmethod
    async def get_listings(self):
        pass


class EtsySearcher(Searcher):
    def __init__(self, session: aiohttp.ClientSession, id_keys: list[str], index_name: str) -> None:
        super().__init__(session, id_keys, index_name)
        self.params = {'limit': 100, 'offset': 0}
        self.headers = {'x-api-key': etsy_api_key}

    async def retrieve_images(self, listing_id):
        async with self.session.get(f'https://openapi.etsy.com/v3/application/listings/{listing_id}/images',
                                    headers={str(i): str(j) for i, j in self.headers.items()}) as response:
            resp = await response.json()
        if not resp.get('results'):
            return []
        return [{'url': img.get('url_fullxfull')} for img in resp.get('results')]

    async def get_listings(self):
        endpoint = 'https://openapi.etsy.com/v3/application/listings/active'
        while True:
            async with self.session.get(endpoint,
                                        params={str(i): str(j)
                                                for i, j in self.params.items()},
                                        headers={str(i): str(j) for i, j in self.headers.items()}) as response:
                if (response.status != 200):
                    logger.debug(response)
                    return
                page = await response.json()

            # add in images for each listing
            listings = [dict(l, **{'images': await self.retrieve_images(l.get('listing_id'))})
                        for l in page.get('results')]
            yield listings
            self.params['offset'] += 100
            if debug_flag:
                break


def get_ebay_auth_token():

    url = "https://api.ebay.com/identity/v1/oauth2/token"

    payload = 'grant_type=client_credentials&scope=https%3A%2F%2Fapi.ebay.com%2Foauth%2Fapi_scope'
    auth_header_data = ebay_client_id + ':' + ebay_client_secret
    encoded_auth_header = base64.b64encode(str.encode(auth_header_data))
    encoded_auth_header = str(encoded_auth_header)[
        2:len(str(encoded_auth_header))-1]
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {encoded_auth_header}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get('access_token')


def extract_values(dictionary, key):
    for k, v in dictionary.items():
        if type(v) is dict:
            if k == key:
                yield v
            yield from extract_values(v, key)
        if type(v) is list:
            for d in v:
                yield from extract_values(d, key)
        elif k == key:
            yield v


def get_ebay_categories(token):
    url = 'https://api.ebay.com/commerce/taxonomy/v1/category_tree/0'
    headers = {
        'Authorization': f'Bearer {token}'}
    response = requests.request('GET', url, headers=headers)
    return response.json()


async def rerun_on_exception(coro, *args, **kwargs):
    while True:
        try:
            logger.warning('running coroutine again...')
            return await coro(*args, **kwargs)
        except asyncio.CancelledError:
            # don't interfere with cancellations
            raise
        except Exception as e:
            logger.error(e, exc_info=True)
            # traceback.print_exc()


class EbaySearcher(Searcher):
    def __init__(self, session: aiohttp.ClientSession, id_keys: list[str], index_name: str) -> None:
        super().__init__(session, id_keys, index_name)
        token = get_ebay_auth_token()
        self.categories = [c for c in extract_values(
            get_ebay_categories(token), 'categoryId')]

    async def try_search(self, client, **kwargs):
        try:
            response: Response[SearchPagedCollection] = await search.asyncio_detailed(
                client=client, **kwargs)
            return response
        except httpx.HTTPError as exc:
            logger.error(exc)

    async def get_listings(self):
        token = get_ebay_auth_token()
        client = AuthenticatedClient(
            base_url='https://api.ebay.com/buy/browse/v1', token=token)
        limit = 200
        for c in self.categories:
            response: Response[SearchPagedCollection] = await rerun_on_exception(search.asyncio_detailed, client=client, limit=limit, category_ids=str(c))
            if response.status_code != 200:
                continue

            response = json.loads(response.content)
            yield response.get('itemSummaries')
            max_listings = min(10000, response.get('total'))

            for offset in range(limit, max_listings, limit):
                response = await self.try_search(client=client, limit=limit, offset=offset, category_ids=str(c), filter=['filter=buyingOptions:{FIXED_PRICE}'])
                # response: Response[SearchPagedCollection] = await rerun_on_exception(search.asyncio_detailed, client=client, limit=limit, offset=offset, category_ids=str(c))
                if response:
                    response = json.loads(response.content)
                    yield response.get('itemSummaries')
            if debug_flag:
                break
