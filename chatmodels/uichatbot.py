from dotenv import load_dotenv
import streamlit as st

load_dotenv()

from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

model = init_chat_model("mistral-small-2506", temperature=0.5)

st.title("Welcome 🎉 (Funny AI Agent)")

# Creating Message history from which my chat model can remember the prev conversation (Short term Memory)
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a sad AI agent feel like crying")
    ]


# Display chat history (skip SystemMessage)
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

prompt = st.chat_input("You : ")

if prompt:
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.write(prompt)

    response = model.invoke(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=response.content))

    with st.chat_message("assistant"):
        st.write(response.content)