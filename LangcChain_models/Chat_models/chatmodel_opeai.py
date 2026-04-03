from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model="gpt-5.4-mini")

result=model.invoke("What is the reason for acid rain")
