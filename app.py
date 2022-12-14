import os
os.system("pip install git+https://github.com/openai/whisper.git")
import streamlit as st
from audiorecorder import audiorecorder
import whisper

model = whisper.load_model("small")

st.title("Audio Recorder")
audio = audiorecorder("Click to record", "Recording...")

if len(audio) > 0:
    # To play audio in frontend:
    st.audio(audio)

    # To save audio to a file:
    wav_file = open("audio.mp3", "wb")
    wav_file.write(audio.tobytes())




print(result["text"])
