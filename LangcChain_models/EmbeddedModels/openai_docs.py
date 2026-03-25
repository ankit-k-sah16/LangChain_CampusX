from langchain_openai import  OpenAIEmbeddings
from  dotenv import load_dotenv

load_dotenv()

document=[
    "A float 32 high precision M.O.E model, quanted in float 32 with additional upgraded and augmented quants too.",
    "It is a Mistral model, max context of 32k (32768) using mixture of experts to combine FOUR top Mistral 7B models into one massive powerhouse at 24B parameters (equal to 28B - 4 X 7 B).",
    "This version 'Enhanced32' is a merge mastered in 'float 32' precision for higher quality and performance."
]
embedding=OpenAIEmbeddings(model="",dimensions=32)

result=embedding.embed_documents(document)

print(str(result))