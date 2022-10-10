import os
import numpy as np
import streamlit as st
from io import BytesIO
import streamlit.components.v1 as components

“–server.enableWebsocketCompression=false”,
“–server.enableXsrfProtection=false”,



def audiorec_demo_app():

    parent_dir = os.path.dirname(os.path.abspath(__file__))
    # Custom REACT-based component for recording client audio in browser
    build_dir = os.path.join(parent_dir, "st_audiorec/frontend/build")
    # specify directory and initialize st_audiorec object functionality
    st_audiorec = components.declare_component("st_audiorec", path=build_dir)

    # TITLE and Creator information
    st.title('streamlit audio recorder')
    st.markdown('Implemented by '
        '[Stefan Rummer](https://www.linkedin.com/in/stefanrmmr/) - '
        'view project source code on '
        '[GitHub](https://github.com/stefanrmmr/streamlit_audio_recorder)')
    st.write('\n\n')


    # STREAMLIT AUDIO RECORDER Instance
    val = st_audiorec()
    # web component returns arraybuffer from WAV-blob
    st.write('Audio data received in the Python backend will appear below this message ...')

    if isinstance(val, dict):  # retrieve audio data
        with st.spinner('retrieving audio-recording...'):
            ind, val = zip(*val['arr'].items())
            ind = np.array(ind, dtype=int)  # convert to np array
            val = np.array(val)             # convert to np array
            sorted_ints = val[ind]
            stream = BytesIO(b"".join([int(v).to_bytes(1, "big") for v in sorted_ints]))
            wav_bytes = stream.read()

        # wav_bytes contains audio data in format to be further processed
        # display audio data as received on the Python side
        st.audio(wav_bytes, format='audio/wav')

if __name__ == '__main__':

    # call main function
    audiorec_demo_app()
