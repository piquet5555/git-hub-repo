import os
from dotenv import load_dotenv
import requests

# Load API key
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

# Read text lines
with open("speech_lines.txt", "r") as f:
    lines = [line.strip() for line in f if line.strip()]

# Define multiple voices and effects (effects are illustrative)
voices = ["alloy", "aria", "echo"]
effects = ["none", "whisper", "robotic"]

# Loop through voices and effects
for voice in voices:
    for effect in effects:
        for idx, line in enumerate(lines):
            filename = f"tts_{voice}_{effect}_{idx+1}.mp3"
            
            payload = {
                "model": "gpt-4o-mini-tts",
                "voice": voice,
                "input": line,
                "effect": effect  # illustrative; actual effect may depend on API support
            }
            
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }
            
            response = requests.post(
                "https://api.openai.com/v1/audio/speech",
                headers=headers,
                json=payload
            )
            
            if response.status_code == 200:
                with open(filename, "wb") as f_out:
                    f_out.write(response.content)
                print(f"Saved {filename}")
            else:
                print(f"Failed for {voice}-{effect}-{idx+1}: {response.text}")
