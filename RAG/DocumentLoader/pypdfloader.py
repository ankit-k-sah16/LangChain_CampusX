from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader("exp1.pdf")

docs=loader.load()
print(type(docs))
print(docs[0].page_content)
print(docs[0].metadata) 