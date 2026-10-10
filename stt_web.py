
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import needle
import tempfile
import os

app = FastAPI(title="Whistle STT API")


@app.get("/")
def home():
    return FileResponse("index.html")


@app.post("/transcribe")
def transcribe(audio: UploadFile = File(...)):
    if audio.content_type not in (
        "audio/wav",
        "audio/x-wav",
        "application/octet-stream",
    ):
        raise HTTPException(400, "Please upload WAV audio")

    path = None

    os.makedirs("recordings", exist_ok=True)

    audio_path = os.path.join("recordings", "mic_recording.wav")

    with open(audio_path, "wb") as f:
        while chunk := audio.file.read(1024 * 1024):
            f.write(chunk)

    result = needle.transcribe(audio_path,
                              language="en")

    return {
            "text": result.get("text", ""),
            "language": result.get("language", ""),
        }


