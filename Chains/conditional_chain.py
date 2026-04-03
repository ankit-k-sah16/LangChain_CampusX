from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.schema.runnable import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_aws import ChatBedrockConverse
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()

model= ChatOllama(model="llama3:8b")

parser= StrOutputParser()

class feedback(BaseModel):
    sentiment: Literal['positive','negative']=Field(description="Give the sentiment of the feedback")


parser2=PydanticOutputParser(pydantic_object=feedback)

prompt1=PromptTemplate(
    template="Classfiy tthe Sentiment of the following  text into POsitive or negative \n {feedback} \n {format_instructions}",
    input_variables=['feedback'],
    partial_variables={'format_instructions':parser2.get_format_instructions()}
)

classifier_chain= prompt1 | model | parser2



prompt2=PromptTemplate(
    template="Write an appropriate response to the following Positive feedback \n{feedback}",
    input_variables=['feedback']
)

prompt3=PromptTemplate(
    template="Write an appropriate response to the following Negative feedback \n{feedback}",
    input_variables=['feedback']
)
branch_chain=RunnableBranch(
    (lambda x:x.sentiment =='positive',prompt2 | model | parser),
    (lambda x:x.sentiment=='negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not find the sentiment of the feedback")
)

chain= classifier_chain | branch_chain

#result=chain.invoke({"feedback": "This is a wonderful product, I'm very satisfied with it."})
#print(result)

result1=chain.invoke({"feedback": "This is such a terrible product, I'm very disappointed with it."})
print(result1)

chain.get_graph()