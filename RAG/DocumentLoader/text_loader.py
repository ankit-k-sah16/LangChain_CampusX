from langchain_community.document_loaders import TextLoader
from langchain_ollama import ChatOllama
loader=TextLoader("exp.txt")
docs=loader.load()
print(type(docs))
print(docs[0].page_content)
print(docs[0].metadata)