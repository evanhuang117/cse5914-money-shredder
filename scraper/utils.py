from abc import abstractmethod
import asyncio
import aiohttp
from logger import logger
from config import *
"""
interleaves two arrays with the same length, with the first element of arr1 as the first element
"""


async def interleave(arr1, arr2):
    result = arr1 + arr2
    result[::2] = arr1
    result[1::2] = arr2
    return result


class Searcher:
    def __init__(self, session: aiohttp.ClientSession, endpoint: str, id_keys: list[str], index_name: str, api_key: str, params={'limit': 100, 'offset': 0}) -> None:
        self.session = session
        self.endpoint = endpoint
        self.headers = {'x-api-key': api_key}
        self.id_keys = id_keys
        self.index_name = index_name
        self.params = params

    async def process_listings(self, listings):
        # create es actions and ids for listings
        actions = [{'update': {'_id': "".join([str(l.get(k)) for k in self.id_keys]),
                               '_index': self.index_name}}
                   for l in listings]
        # replace newline chars in text bc bulk uses new line delimited json
        listings = [{key: value.replace('\n', '') if isinstance(value, str) else value
                    for key, value in l.items()}
                    for l in listings]
        # add in images for each listing
        listings = [dict(l, **{'images': await self.retrieve_images(l.get('listing_id'))})
                    for l in listings]

        # create docs to upsert
        # add upsert=true to all results
        listings = [{'doc': l, 'doc_as_upsert': 'true'} for l in listings]
        return await interleave(actions, listings)

    async def get_bulk_actions(self):
        while True:
            async with self.session.get(self.endpoint,
                                        params={str(i): str(j)
                                                for i, j in self.params.items()},
                                        headers={str(i): str(j) for i, j in self.headers.items()}) as response:
                if (response.status != 200):
                    logger.debug(response)
                    return
                page = await response.json()
            yield await self.process_listings(page.get('results'))
            self.params['offset'] += 100
            if debug_flag:
                break

    @abstractmethod
    async def retrieve_images(self):
        pass


class EtsySearcher(Searcher):
    async def retrieve_images(self, listing_id):
        async with self.session.get(f'https://openapi.etsy.com/v3/application/listings/{listing_id}/images',
                                    headers={str(i): str(j) for i, j in self.headers.items()}) as response:
            resp = await response.json()
        return [{'url': img.get('url_fullxfull')} for img in resp.get('results')]
