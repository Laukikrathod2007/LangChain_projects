from langchain_OpenAI import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

prompt = PromptTemplate(
    template ="Give me most powerful {gender} anime character",
    input_variables= ['gender']
)
model = ChatOpenAI()
parser = StrOutputParser()

chain = prompt | model |parser

result =chain.invoke({'gender':'female'}) 
print(result)