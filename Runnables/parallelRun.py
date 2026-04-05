from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables.base import RunnableParallel,RunnableSequence

load_dotenv()

prompt1=PromptTemplate(
    template=" Write a tweet about the  {topic}",
    input_variables=['topic']
    )

prompt2=PromptTemplate(
    template='Generate a LinkedIn post about the - {topic}',
    input_variables=['topic']
)
model1=ChatOllama(model='llama3:8b')

model2=ChatOllama(model='qwen3.5:latest')

parser=StrOutputParser()

parallel_chain=RunnableParallel(
    {
    'tweet':RunnableSequence(prompt1,model1,parser),
     'linkedin':RunnableSequence(prompt2,model2,parser)})

result=parallel_chain.invoke({'topic':'AI'})
print(result)