import streamlit as st
import openai
import os


client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])

audio_file = st.experimental_audio_input("Record a voice message")

if st.button("Transcribe"):
    if audio_file:
        transcript = client.audio.translations.create(
            model="whisper-1",
            file=audio_file,
            response_format="text"
        )
        st.subheader("Transcription:")
        st.write(transcript)
    else:
        st.error("Audio is not clear or not recorded.")