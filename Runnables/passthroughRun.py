from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables.base import RunnableParallel,RunnableSequence,RunnableLambda
from langchain_core.runnables import RunnablePassthrough
load_dotenv()

prompt=PromptTemplate(
    template=" Write a joke about  {topic}",
    input_variables=['topic']
    )


model=ChatOllama(model='qwen3.5:latest')

parser=StrOutputParser()

joke_genchain=RunnableSequence(prompt,model,parser)

parallel_chain=RunnableParallel(
    {
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(lambda x:len(x.split()))})

final_chain=RunnableSequence(joke_genchain,parallel_chain)
result=final_chain.invoke({'topic':'AI'})
final_result="""{} \n word count -{}""".format(result['joke'],result['word_count'])

print(final_result)

    