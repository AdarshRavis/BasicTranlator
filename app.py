import streamlit as st
from audiorecorder import audiorecorder
import whisper

    

st.title("Audio Recorder")
audio = audiorecorder("Click to record", "Recording...")

if len(audio) > 0:
    # To play audio in frontend:
    st.audio(audio)

    # To save audio to a file:
    wav_file = open("audio.mp3", "wb")
    wav_file.write(audio.tobytes())


!whisper "Oh Captain My Captain by Walt Whitman.mp3" --model medium

print(result["text"])
