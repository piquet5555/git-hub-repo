from dotenv import load_dotenv
import os

# Load .env file in project root
load_dotenv()

# Minimal test: check if API key is loaded
api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("OPENAI_API_KEY loaded successfully (key hidden).")
else:
    print("OPENAI_API_KEY not found. Check your .env file.")
