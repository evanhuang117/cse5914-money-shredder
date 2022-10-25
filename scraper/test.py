import asyncio
import json
import aiohttp
from ebay_browse_api_client.ebay_browse_api_client.client import AuthenticatedClient
from ebay_browse_api_client.ebay_browse_api_client.api.item_summary import search
import utils
from utils import EbaySearcher
from pprint import pprint

async def main():
    ebay_session = aiohttp.ClientSession()
    e = EbaySearcher(ebay_session, ['itemId'], 'ebay')
    token = utils.get_ebay_auth_token()
    client = AuthenticatedClient(
        base_url='https://api.ebay.com/buy/browse/v1', token=token)
    response = await search.asyncio_detailed(client=client, limit=10, q='spoon', filter_=['filter=buyingOptions:{FIXED_PRICE}'])
    pprint(json.loads(response.content).get('itemSummaries'))

if __name__ == '__main__':
    asyncio.run(main())