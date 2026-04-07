from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables.base import RunnableParallel,RunnableSequence,RunnableLambda
from langchain_core.runnables import RunnablePassthrough,RunnableBranch


load_dotenv()

prompt1=PromptTemplate(
    template=" Write a detailed note on the {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template=" Summarize the following text \n {text}",
    input_variables=['text']
)

model=ChatOllama(model='qwen3.5:latest')
parser=StrOutputParser()

report_gen_chain=RunnableSequence(prompt1,model,parser)

branch_chain=RunnableBranch(
    (lambda x:len(x.split())>500,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain=RunnableSequence(report_gen_chain,branch_chain)
print(final_chain.invoke({'topic':"Russia-Ukraine War"}))