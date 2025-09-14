# Load API key from .env
$env:OPENAI_API_KEY = (Get-Content ".env" | Where-Object { $_ -match "^OPENAI_API_KEY=" }).Split('=')[1].Trim()

# Short test phrase
$TEXT = "Hello from Yale AI class"

# Headers and JSON body
$headers = @{
    "Authorization" = "Bearer $env:OPENAI_API_KEY"
    "Content-Type"  = "application/json"
}

$body = @{
    model = "gpt-4o-mini-tts"
    voice = "alloy"
    input = $TEXT
} | ConvertTo-Json

# Make TTS request and save output
Invoke-RestMethod -Uri "https://api.openai.com/v1/audio/speech" `
    -Method POST `
    -Headers $headers `
    -Body $body `
    -OutFile "test.mp3"

# Check if file exists
if (Test-Path "test.mp3") {
    Write-Output "TTS succeeded - test.mp3 generated!"
    Start-Process "test.mp3"
} else {
    Write-Error "TTS failed - no output file."
}







