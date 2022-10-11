from distutils.log import debug
import os

from dotenv import load_dotenv
from logger import logger

# load secrets from .env file
load_dotenv()

user_agent = os.getenv("USER_AGENT")
etsy_api_key = os.getenv("ETSY_API_KEY")
debug_flag = False if os.getenv("DEBUG").lower() == 'false' else True
logger.info(f'DEBUG FLAG: {debug_flag}')