import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()
# Generate embedding
response = client.models.embed_content(
    model="gemini-embedding-001",
    contents="Generative AI is transforming the world."
)

# Get the embedding vector
embedding = response.embeddings[0].values

print(f"Embedding Dimensions: {len(embedding)}")
print("\nFirst 10 values:")
print(embedding[:10])