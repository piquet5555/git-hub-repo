import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not set in .env!")

# The text you want to convert to speech
text = "Hello from Yale AI class. This is a short TTS test."

# TTS request using OpenAI API
url = "https://api.openai.com/v1/audio/speech"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
json_data = {
    "model": "gpt-4o-mini-tts",
    "voice": "alloy",
    "input": text
}

response = requests.post(url, headers=headers, json=json_data)

# Save response to MP3 if successful
if response.status_code == 200:
    with open("test.mp3", "wb") as f:
        f.write(response.content)
    print("TTS succeeded — saved test.mp3")
else:
    print(f"TTS failed: {response.status_code}, {response.text}")

