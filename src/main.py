import getpass
import os
import streamlit as st
from dotenv import load_dotenv

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
from langchain.chat_models import init_chat_model


load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_BASE_URL"] = "https://models.github.ai/inference"

message_history = []

model = init_chat_model("gpt-4.1-mini", model_provider="openai")

msg = model.invoke([HumanMessage(content="Hi! I'm Bob")])

# model = ChatOpenAI(model="gpt-4.1-mini")

# msg = model.invoke(
#     [HumanMessage(content="Hi! I'm sam!"),
#     AIMessage(content="hi, how can i assist"),
#     HumanMessage(content="Hi! whats my name")]
# )

print(msg.content)


# def history_loader(session_id: str):
#     pass


# RunnableWithMessageHistory(model, get_session_history=history_loader)


st.set_page_config(page_title="Buddy", page_icon="🤖")

st.title("Buddy")
st.write("Your friendly ai bot")

user_msg = st.chat_input(placeholder="What's in your mind")

if user_msg:
    print("msg: ", user_msg)

