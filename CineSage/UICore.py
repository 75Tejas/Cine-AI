import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from typing import List, Optional

# Load environment variables
load_dotenv()

# Initialize model
model = ChatMistralAI(model="mistral-small-2506")

# -------------------------------
# Pydantic Schema
# -------------------------------
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

# Output Parser
parser = PydanticOutputParser(pydantic_object=Movie)

# Prompt
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
Extract movie information from the paragraph.

{format_instructions}
        """
    ),
    (
        "human",
        "{paragraph}"
    )
])

# Chain for Raw Output
raw_chain = prompt | model

# Chain for Structured Output
structured_chain = prompt | model | parser

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(
    page_title="🎬 CineSage",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 CineSage")
st.write("Extract structured movie information from a movie description.")

paragraph = st.text_area(
    "Movie Description",
    height=250,
    placeholder="Paste the movie description here..."
)

if st.button("Extract Information", use_container_width=True):

    if not paragraph.strip():
        st.warning("Please enter a movie description.")
    else:

        inputs = {
            "paragraph": paragraph,
            "format_instructions": parser.get_format_instructions()
        }

        with st.spinner("Extracting..."):

            # Raw LLM Output
            raw_response = raw_chain.invoke(inputs)

            # Structured Output
            movie = structured_chain.invoke(inputs)

        st.success("Information Extracted!")

        st.subheader("Raw Model Output")
        st.code(raw_response.content, language="json")

        st.subheader("Structured Output")
        st.json(movie.model_dump())