import needle

result = needle.transcribe("recordings/mic_recording.wav")

print(result)
print("Text:", result["text"])