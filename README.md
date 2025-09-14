## Environment & quick start

Create and activate a local Python virtual environment:
  python -m venv env
  .\env\Scripts\Activate    # PowerShell

Install dependencies:
  python -m pip install --upgrade pip
  python -m pip install openai "openai[voice_helpers]" sounddevice numpy python-dotenv

Select the interpreter in VS Code: use the env interpreter at `.\env\Scripts\python.exe`.

Minimal test to confirm environment variables load:
  python 1_streaming_tts_test.py

