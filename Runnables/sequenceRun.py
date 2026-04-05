from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.base import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

prompt1=PromptTemplate(
    template=" Write a joke about the following {topic}",
    input_variables=['topic']
    )

prompt2=PromptTemplate(
    template='Explain the joke - {text}',
    input_variables=['text']
)
model=ChatOllama(model='llama3:8b')

parser=StrOutputParser()

chain=RunnableSequence(prompt1,model,parser,prompt2,model,parser)

result=chain.invoke({'topic':'AI'})
print(result)