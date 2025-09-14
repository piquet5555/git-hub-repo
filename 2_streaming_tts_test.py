import os
from dotenv import load_dotenv
import openai
import sounddevice as sd
import numpy as np
import io
import soundfile as sf

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Read text from file
with open("narration.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Request TTS
response = openai.audio.speech.create(
    model="gpt-4o-mini-tts",
    voice="alloy",
    input=text
)

# Convert bytes to playable waveform
audio_bytes = response
with io.BytesIO(audio_bytes) as f:
    data, samplerate = sf.read(f)
    sd.play(data, samplerate)
    sd.wait()






