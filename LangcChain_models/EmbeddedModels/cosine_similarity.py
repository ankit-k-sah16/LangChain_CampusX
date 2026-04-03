from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding=OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)

document=["A float 32 high precision M.O.E model, quanted in float 32 with additional upgraded and augmented quants too.",
    "It is a Mistral model, max context of 32k (32768) using mixture of experts to combine FOUR top Mistral 7B models into one massive powerhouse at 24B parameters (equal to 28B - 4 X 7 B).",
    "This version 'Enhanced32' is a merge mastered in 'float 32' precision for higher quality and performance."]

query="Tell me about Enhanced32?"

document_embedding=embedding.embed_documents(document)
query_enbedding=embedding.embed_query(query)

scores=cosine_similarity([query_enbedding],document_embedding)

index,score=sorted(list(enumerate(score)),key=lambda x:x[1])[-1]

print(query)
print(document[index])
print("Similarity Score is:",score)
