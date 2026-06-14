from openai import OpenAI
from config import BASE_URL, API_KEY

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)
