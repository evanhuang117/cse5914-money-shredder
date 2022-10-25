from elasticsearch.exceptions import ConnectionError
from elasticsearch import AsyncElasticsearch
import asyncio
import aiohttp
from logger import logger
from config import *
from utils import EbaySearcher, EtsySearcher
from pprint import pprint, PrettyPrinter


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

    logger.info('connected to es')
    etsy_session = aiohttp.ClientSession()
    ebay_session = aiohttp.ClientSession()

    searchers = [EtsySearcher(
        etsy_session, ['listing_id', 'user_id', 'shop_id'], 'etsy'),
        EbaySearcher(ebay_session, ['itemId'], 'ebay')]
    loop = asyncio.get_event_loop()

    search_tasks = [do_stuff_periodically(
        60*60*24, insert_elasticsearch, es, loop, s.get_bulk_actions()) for s in searchers]

    await asyncio.gather(*search_tasks)


async def insert_elasticsearch(es, loop, bulk_actions):
    async for listings in bulk_actions:
        if debug_flag:
            logger.debug(PrettyPrinter().pformat(listings[:2]))
        asyncio.ensure_future(es.bulk(body=listings), loop=loop)
    logger.info('finished updating es')


async def do_stuff_periodically(interval, periodic_function, *args):
    while True:
        logger.debug("Starting periodic function")
        await asyncio.gather(
            asyncio.sleep(interval),
            periodic_function(*args)
        )


if __name__ == '__main__':
    asyncio.run(main())
