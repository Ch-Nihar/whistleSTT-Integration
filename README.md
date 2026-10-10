# Cactus Whistle STT Integration using FastAPI

A small local speech-to-text (STT) demo using **Cactus Whistle** with a **FastAPI** backend and a browser-based microphone interface.

## Features

- Record speech from the browser microphone.
- Convert recorded audio to **16 kHz, mono, 16-bit PCM WAV**.
- Send the WAV recording to a local FastAPI endpoint.
- Transcribe the audio using `needle.transcribe()`.
- Display the recognized text in the webpage.

## Requirements

- Python installed
- A working Cactus Whistle / `needle` installation
- Chrome or Edge
- FastAPI, Uvicorn, and `python-multipart`

Install the web API dependencies in the same Python environment where Whistle works:

```bash
python -m pip install fastapi uvicorn python-multipart
```

## Run locally

1. Activate the virtual environment used for your working Whistle installation.
2. Make sure `stt_web.py` and `index.html` are in the project directory.
3. Start the server:

   ```bash
   python -m uvicorn stt_web:app --host 127.0.0.1 --port 5000
   ```

4. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in Chrome or Edge.
5. Allow microphone access, click **Start recording**, speak, and click **Stop & transcribe**.

The backend should expose `GET /` to serve `index.html` and `POST /transcribe` to receive a WAV file and return JSON containing `text` and optionally `language`.

## Test transcription directly

If your existing test script uses `needle.transcribe()`, you can test a saved WAV recording directly:

```python
import needle

result = needle.transcribe("recordings/mic_recording.wav")
print(result)
```

## Notes

- Keep recordings short for this starter demo.
- Microphone access normally requires `localhost`/`127.0.0.1` or HTTPS.
- Transcription accuracy depends on recording quality, preprocessing, language support, and model settings.
- Do not commit your virtual environment, private credentials, logs, or large audio recordings.
- Adapt filenames and commands if your project uses different names.
