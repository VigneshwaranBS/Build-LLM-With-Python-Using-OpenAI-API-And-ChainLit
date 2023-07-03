import os 
from langchain import PromptTemplate , OpenAI , LLMChain
import chainlit as cl
# from constants import openai_key

openai_key="REPLACE YOUR OWN OPENAI KEY HERE"

os.environ["OPENAI_API_KEY"] = openai_key
 
template = """Question :{question}

Answer : let's think the answer.""" 
 
@cl.langchain_factory(use_async=True)
def factory():
    prompt = PromptTemplate(template=template,input_variables=["question"])
    llm_chain =LLMChain(prompt=prompt,llm=OpenAI(template=0),verbose=True)
    
    return llm_chain