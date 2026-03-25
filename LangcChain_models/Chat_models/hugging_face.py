from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace

model_id = "mistralai/Mistral-7B-Instruct-v0.2"

# Load tokenizer + correct model class
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# Create pipeline manually
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    temperature=0.5,
    max_new_tokens=100
)

# Wrap in LangChain
llm = HuggingFacePipeline(pipeline=pipe)
chat_model = ChatHuggingFace(llm=llm)

# Run
result = chat_model.invoke("What was the reason of Soviet Decline?")
print(result.content)