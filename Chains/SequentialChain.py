from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt1=PromptTemplate(
    template="Generate a detailed report on the {topic}",
    input_variables=['topic'])

prompt2=PromptTemplate(
    template="Summarize the following report in 5 sentences: {report}",
    input_variables=['report']
)

model=ChatOllama(model="llama3:8b")

parser=StrOutputParser()

chain= prompt1 | model | parser | prompt2 | model | parser
result= chain.invoke({'topic':"Creatine Monohydrate"})

print(result)