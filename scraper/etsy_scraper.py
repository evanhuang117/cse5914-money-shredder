from elasticsearch.exceptions import ConnectionError
from elasticsearch import AsyncElasticsearch, Elasticsearch
from elasticsearch.helpers import async_bulk
import asyncio
import aiohttp
from logger import logger
from config import *
import time


async def update_elasticsearch(session):
    async_bulk(es, get_listings(session))


async def get_listings(session, params={'limit': 100, 'offset': 0}, search_string=""):
    headers = {'User-Agent': user_agent}
    async with session.get(f"https://openapi.etsy.com/v3/application/listings/active", params=params) as response:
        if (response.status != 200):
            raise StopAsyncIteration()
        page = await response.json()
    yield page.get('results')
    params['offset'] += 100
    yield get_listings(session, search_string, params)


async def do_stuff_periodically(interval, periodic_function):
    while True:
        print("Starting periodic function")
        await asyncio.gather(
            asyncio.sleep(interval),
            periodic_function(),
        )


if __name__ == '__main__':
    es = Elasticsearch(hosts=[{'host': 'elasticsearch',
                               'port': 9200,
                               'scheme': 'http'}], retry_on_timeout=True)
    for _ in range(100):
        try:
            # make sure the cluster is available
            es.cluster.health(wait_for_status="yellow")
        except ConnectionError:
            time.sleep(2)

    print('connected')
    session = aiohttp.ClientSession()
    asyncio.run(do_stuff_periodically(
        60*60*24, lambda: update_elasticsearch(session)))
