fromlangchain_core.output_parsers import PydanticOutputParser
from pydantic import BAseModel,Field
from lamgchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="google/gemma-2b-it",
    task="text-generation")

model=ChatHuggingFace(llm=llm)

class Person(BaseModel):

    name:str=Field(description="Name of the person")
    age: int=Field(description="Age of the person")
    city:str=Field(description="City of the person")

parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template="Give me the name,age and city of a frictional {place} person. \n {format_instruction}",
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
    )

prompt=template.invoke({'place':'Spain'})

result=model.invoke(prompt)

final_result=parser.parse(result.content)
print(final_result) 