import streamlit as st
from audiorecorder import audiorecorder
import whisper
from keras.models import load_model

    
model = whisper.load_model("base")

st.title("Audio Recorder")
audio = audiorecorder("Click to record", "Recording...")

if len(audio) > 0:
    # To play audio in frontend:
    st.audio(audio)

    # To save audio to a file:
    wav_file = open("audio.mp3", "wb")
    wav_file.write(audio.tobytes())


result = model.transcribe("audio.mp3")
print(result["text"])
