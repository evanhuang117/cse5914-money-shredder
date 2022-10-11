from elasticsearch.exceptions import ConnectionError
from elasticsearch import AsyncElasticsearch
import asyncio
import aiohttp
from logger import logger
from config import *


async def main():
    es = AsyncElasticsearch(hosts=[{'host': 'elasticsearch',
                                    'port': 9200,
                                    'scheme': 'http'}], retry_on_timeout=True)
    for _ in range(100):
        try:
            # make sure the cluster is available
            await es.cluster.health(wait_for_status="yellow")
        except ConnectionError:
            await asyncio.sleep(2)

    logger.info('connected')
    session = aiohttp.ClientSession()
    loop = asyncio.get_event_loop()
    await do_stuff_periodically(
        60*60*24, update_elasticsearch, es, session, loop)


async def update_elasticsearch(es, session, loop):
    i = 0
    async for listings in get_listings(session):
        bulk_actions = await process_listings(listings)
        logger.debug(bulk_actions[:2])
        asyncio.ensure_future(es.bulk(body=bulk_actions), loop=loop)
        # logger.debug(f"ES ERRORS: {resp.get('errors')}")
        i += len(listings)
    logger.info('finished updating es')
    return i


async def process_listings(listings):
    # create es actions and ids for listings
    actions = [{'update': {'_id': f"{l.get('listing_id')}{l.get('user_id')}{l.get('shop_id')}",
                           '_index': 'etsy'}}
               for l in listings]
    # replace newline chars in text bc bulk uses new line delimited json
    listings = [{key: value.replace('\n', '') if isinstance(value, str) else value
                 for key, value in l.items()}
                for l in listings]
    # create docs to upsert
    # add upsert=true to all results
    listings = [{'doc': l, 'doc_as_upsert': 'true'} for l in listings]
    return await interleave(actions, listings)


"""
interleaves two arrays with the same length, with the first element of arr1 as the first element
"""


async def interleave(arr1, arr2):
    result = arr1 + arr2
    result[::2] = arr1
    result[1::2] = arr2
    return result


async def get_listings(session, params={'limit': 100, 'offset': 0}, search_string="", headers={'x-api-key': etsy_api_key}):
    while True:
        async with session.get(f"https://openapi.etsy.com/v3/application/listings/active", params={str(i): str(j) for i, j in params.items()}, headers={str(i): str(j) for i, j in headers.items()}) as response:
            if (response.status != 200):
                logger.debug(response)
                return
            page = await response.json()
        yield page.get('results')
        params['offset'] += 100
        if debug_flag:
            break


async def do_stuff_periodically(interval, periodic_function, *args):
    while True:
        logger.debug("Starting periodic function")
        await asyncio.gather(
            asyncio.sleep(interval),
            periodic_function(*args)
        )


if __name__ == '__main__':
    asyncio.run(main())
