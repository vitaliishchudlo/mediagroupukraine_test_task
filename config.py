import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = str(os.getenv("API_KEY"))
