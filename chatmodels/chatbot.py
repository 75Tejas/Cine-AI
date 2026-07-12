from dotenv import load_dotenv
import os

load_dotenv()

from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage


model = init_chat_model("mistral-small-2506" ,temperature=0,max_tokens = 20)

#Creating Message history from which my chat model can remember the prev conversation(Short term Memory)

print("choose AI Mode")
print("press 1 forAngry mode")
print("press 2 for funny mode")
print("press 3 for sad mode")
choice = int(input("tell your response : -"))

if choice ==1:
    mode = "You are very angry AI agent. You respond aggressively and impatiently."
elif choice ==2:
    mode = "You are a funny AI agent. You respond with humor and jokes."
elif choice ==3:
    mode="You are Sad AI agent."  
         
messages = [
    SystemMessage(content=mode)
]

print("----------------Welcome type 0 to exit the application----------------")

while True:
    prompt = input("You : ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))  
    print("Bot: ",response.content)
    

