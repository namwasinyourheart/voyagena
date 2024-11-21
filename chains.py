from prompts import gen_itinerary_prompt
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from schemas import UserInput

from utils import extract_itinerary,  convert_to_trip_plan

def get_llm():
    llm = ChatOpenAI(model="gpt-4o-mini", 
                     temperature=0.7, 
                     max_tokens=2000)
    return llm

def get_embeddings():
    embeddings = OpenAIEmbeddings()
    return embeddings


def get_gen_itinerary_chain():
    llm = get_llm()
    gen_itinerary_chain = gen_itinerary_prompt | llm | StrOutputParser() | extract_itinerary | convert_to_trip_plan
    
    return gen_itinerary_chain


def get_itinerary(user_input: UserInput):
    gen_itinerary_chain = get_gen_itinerary_chain()

    itinerary = gen_itinerary_chain .invoke(user_input.dict())

    return itinerary