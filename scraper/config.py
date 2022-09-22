import os

from dotenv import load_dotenv

# load secrets from .env file
load_dotenv()

user_agent = os.getenv("USER_AGENT")
etsy_api_key = os.getenv("ETSY_API_KEY")