import os

from dotenv import load_dotenv
from logger import logger

# load secrets from .env file
load_dotenv()

user_agent = os.getenv("USER_AGENT")
etsy_api_key = os.getenv("ETSY_API_KEY")
ebay_client_id = os.getenv("EBAY_CLIENT_ID")
ebay_client_secret = os.getenv("EBAY_CLIENT_SECRET")
debug_flag = False if os.getenv("DEBUG").lower() == 'false' else True
logger.info(f'DEBUG FLAG: {debug_flag}')