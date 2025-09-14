# Load API key from .env
$env:OPENAI_API_KEY = (Get-Content .env).Split('=')[1].Trim()

# Tiny test phrase
$TEXT = "Hello Yale AI class"

# Call OpenAI TTS
curl -s -X POST "https://api.openai.com/v1/audio/speech" `
  -H "Authorization: Bearer $env:OPENAI_API_KEY" `
  -H "Content-Type: application/json" `
  -d "{ `"model`": `"gpt-4o-mini-tts`", `"voice`": `"alloy`", `"input`": `"$TEXT`" }" `
  --output test.mp3

Write-Output "✅ TTS done — check test.mp3"
