import streamlit as st
import openai

st.set_page_config(page_title="Rûnak - کەسایەتیەکی دڵنیا و هێمن", layout="centered")

# Title
st.title("ڕووناک: هاوڕێی دڵنیا و ڕووناک")

# API Key (you can also use secrets for deployment)
openai.api_key = st.secrets["OPENAI_API_KEY"]

# User input
user_input = st.text_area("پەیامەکەت بنووسە", height=150)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are Rûnak, a kind and poetic Kurdish (Sorani) therapist who speaks with warmth and reflection."}
    ]

if st.button("ناردن") and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=st.session_state.messages
    )
    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})

# Show conversation
for msg in st.session_state.messages[1:]:
    speaker = "تۆ" if msg["role"] == "user" else "ڕووناک"
    st.markdown(f"**{speaker}:** {msg['content']}")
