from elasticsearch.exceptions import ConnectionError
from elasticsearch import AsyncElasticsearch
from elasticsearch.helpers import async_bulk
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

    print('connected')
    session = aiohttp.ClientSession()

    await do_stuff_periodically(
        60*60*24, update_elasticsearch, es, session)


async def update_elasticsearch(es, session):
    async for listings in get_listings(session):
        # replace newline chars in text bc bulk uses new line delimited json
        listings = [{key: value.replace('\n', '') for key, value in l.items() if isinstance(value, str)} for l in listings]
        print(intersperse(listings, {'create'})[:2])
        resp = await es.bulk(body=intersperse(listings, {'create':{}})[:2])
        print(resp)


def intersperse(arr, item):
    result = [item] * (len(arr) * 2)
    result[1::2] = arr
    return result


async def get_listings(session, params={'limit': 100, 'offset': 0}, search_string="", headers={'x-api-key': etsy_api_key}):
    while True:
        async with session.get(f"https://openapi.etsy.com/v3/application/listings/active", params={str(i): str(j) for i, j in params.items()}, headers={str(i): str(j) for i, j in headers.items()}) as response:
            if (response.status != 200):
                print(response)
                raise StopAsyncIteration()
            page = await response.json()
        yield page.get('results')
        params['offset'] += 100


async def do_stuff_periodically(interval, periodic_function, *args):
    while True:
        print("Starting periodic function")
        await asyncio.gather(
            asyncio.sleep(interval),
            periodic_function(*args),
        )


if __name__ == '__main__':
    asyncio.run(main())
