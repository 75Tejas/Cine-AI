from dotenv import load_dotenv
import os
# Load  env variable from your .env file into your python program.
load_dotenv()
#initalize
from langchain.chat_models import init_chat_model

model = init_chat_model("google_genai:gemini-2.5-flash-lite" ,temperature=0,max_tokens = 20)
#after invoking model store it in response variable and run the file.
response = model.invoke("The sky is...")

print(response)
