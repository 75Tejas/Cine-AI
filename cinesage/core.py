from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
import os
from langchain_mistralai import ChatMistralAI
from pydantic import BaseModel
from typing import List,Optional
from langchain_core.output_parsers import PydanticOutputParser
load_dotenv()
model = ChatMistralAI(model = 'mistral-small-2506')

#Creating Schema
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str] 
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

#Creating Parser check the schema

parser = PydanticOutputParser(pydantic_object=Movie)


#prompt is runnable

prompt = ChatPromptTemplate.from_messages([
    ('system', """
     Extract movie information from the paragraph
     {format_instructions}
     """),
    ("human","{paragraph}")
])

#After Creating Prompt temp you ask user for paragraph

para = input("Give your paragraph: ")

#final prompt

final_prompt = prompt.invoke(
    {"paragraph" : para,
     'format_instructions': parser.get_format_instructions()}
)

response = model.invoke(final_prompt)
movie = parser.parse(response.content)

print(movie)
