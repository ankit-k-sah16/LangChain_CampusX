from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFacePipeline.from_model_id(
    model_id="nvidia/Nemotron-Cascade-2-30B-A3B",task="text-generation")

model=ChatHuggingFace(llm=llm)

chat_history=[]

while True:
    user_input=input("You: ")
    chat_history.append(user_input)
    if user_input==exit:
        break
    result=model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ", result.content)

print(chat_history) 
