import os

from dotenv import load_dotenv

# load secrets from .env file
load_dotenv()

user_agent = os.getenv("USER_AGENT")

search_string = ""
post_update_interval_seconds = 5
search_result_limit = 30

