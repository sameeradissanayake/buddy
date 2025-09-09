import os
import streamlit as st
from dotenv import load_dotenv

from langchain.chat_models import init_chat_model


load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_BASE_URL"] = "https://models.github.ai/inference"


if "message_history" not in st.session_state:
    st.session_state.message_history = []

model = init_chat_model("gpt-4.1-mini", model_provider="openai")

st.set_page_config(page_title="Buddy", page_icon="./src/resources/buddy.png")

st.title("Buddy")
st.subheader("Your friendly ai bot")


user_input = st.chat_input(placeholder="What's in your mind")


for message in st.session_state.message_history:
    if message["role"] == "ai":
        with st.chat_message("assistant", avatar="./src/resources/buddy.png"):
            st.markdown(message["content"])
    elif message["role"] == "human":
        with st.chat_message("human", avatar="./src/resources/human.png"):
            st.markdown(message["content"])

if user_input:

    with st.chat_message("human", avatar="./src/resources/human.png"):
            st.markdown(user_input)

    st.session_state.message_history.append({"role": "human", "content": user_input})

    ai_msg = model.invoke(st.session_state.message_history)

    st.session_state.message_history.append({"role": "ai", "content": ai_msg.content})
    
    with st.chat_message("assistant", avatar="./src/resources/buddy.png"):
        st.markdown(ai_msg.content)
