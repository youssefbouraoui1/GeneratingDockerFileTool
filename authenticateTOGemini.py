import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

def authenticate():
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set in .env")
    client = genai.Client(api_key= api_key)
    return client

print("hello")