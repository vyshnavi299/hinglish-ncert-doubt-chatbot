import streamlit as st
import openai
from gtts import gTTS
import os

openai.api_key = "YOUR_OPENAI_API_KEY"

st.title("📚 Hinglish NCERT Doubt Chatbot")

user_question = st.text_input("Ask your doubt (Hinglish / Tanglish allowed)")

if st.button("Get Explanation"):

    prompt = f"""
You are a helpful senior student explaining NCERT Class 9-10 science or maths concepts.

Rules:
- Answer in Hinglish
- Use simple explanations
- Use Indian examples like cricket, dal, chai
- Only answer NCERT Class 9-10 topics
- If outside syllabus say politely it's outside NCERT 9-10

Student question:
{user_question}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    answer = response['choices'][0]['message']['content']

    st.write("### Explanation")
    st.write(answer)

    # Text to Speech
    tts = gTTS(answer)
    tts.save("voice.mp3")

    audio_file = open("voice.mp3", "rb")
    st.audio(audio_file.read())
