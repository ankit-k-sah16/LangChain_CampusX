from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
load_dotenv()

model=ChatOllama(model="llama3:8b")

st.header("Research Tool")

paper_input=st.selectbox("Select Research Paper Name",["Attention is All You Need",
"BERT:Pre-training of Deep Bidirectional Transformers",
"GPT-3: Language Models are Few-Shot Learners"
])

style_input=st.selectbox("Select Explanation Style",["Beginner-Friendly", "Technical","Code-Oriented","Mathematical"])

length_input=st.selectbox("Select Explanation Length",["Short  (1-2 paragraph)",
"Medium (3-5 paragraph)","Long (6-8 paragraphs)"])

#template
template=load_prompt("template.json")

#fill the placeholders

#prompt=template.invoke({
   # 'paper_input':paper_input,
   # 'style_input':style_input,
   # 'length_input':length_input


if st.button('Summarize'):

    chain= template | model
    result=chain.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input})

    ##result=model.invoke(prompt)
    
    st.write(result.content)