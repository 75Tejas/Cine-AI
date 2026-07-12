from dotenv import load_dotenv
import os
# Load  env variable from your .env file into your python program.
load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    temperature=0.7,
    max_new_tokens=20,
)
model = ChatHuggingFace(llm=llm)

response = model.invoke("the sky is...")

print(response.content)