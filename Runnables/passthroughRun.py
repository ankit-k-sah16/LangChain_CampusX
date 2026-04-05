from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables.base import RunnableParallel,RunnableSequence
from langchain_core.runnables import RunnablePassthrough
load_dotenv()

prompt1=PromptTemplate(
    template=" Write a joke about  {topic}",
    input_variables=['topic']
    )

prompt2=PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

model=ChatOllama(model='qwen3.5:latest')

parser=StrOutputParser()

joke_genchain=RunnableSequence(prompt1,model,parser)

parallel_chain=RunnableParallel(
    {
    'joke':RunnablePassthrough(),
     'explanation':RunnableSequence(prompt2,model,parser)})

final_chain=RunnableSequence(joke_genchain,parallel_chain)
print(final_chain.invoke({'topic':'AI'}))

    