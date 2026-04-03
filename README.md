#  LangChain Learning Repository

##  Overview

This repository contains my hands-on exploration of **LangChain**, where I’ve implemented various **basic to intermediate-level concepts** to understand how LLM-powered applications are built.

The goal of this repo is to break down LangChain components into simple, practical code examples and demonstrate how they work internally.

---

##  Objectives

* Understand core components of LangChain
* Build intuition around LLM workflows
* Experiment with chaining, prompting, and output parsing
* Create a strong foundation for real-world AI applications

---

##  Topics Covered

### 🔹 1. LLMs & Chat Models

* Using different LLM providers
* Chat vs completion models
* Temperature, max tokens, etc.

### 🔹 2. Prompt Templates

* Dynamic prompts using `PromptTemplate`
* ChatPromptTemplate usage
* Role-based prompting

### 🔹 3. Chains

* Simple Chains
* Sequential Chains
* LLMChain
* Combining multiple components

### 🔹 4. Output Parsers

* Structured output parsing
* `StrOutputParser`
* Custom output formatting

### 🔹 5. Memory (if included)

* ConversationBufferMemory
* Maintaining chat history

### 🔹 6. LangChain Pipelines

* Combining prompts + models + parsers
* End-to-end flow creation

---

## ⚙️ Tech Stack

* Python 🐍
* LangChain 🦜🔗
* HuggingFace / OpenAI (depending on usage)
* Jupyter Notebook / Python Scripts

---

## 📂 Project Structure

```
LangChain/
│
├── prompts/
├── chains/
├── output_parsers/
├── memory/
├── examples/
├── notebooks/
└── README.md
```

---

##  Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/langchain-learning.git
cd langchain-learning
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set up API keys

Create a `.env` file and add:

```
OPENAI_API_KEY=your_api_key
HUGGINGFACEHUB_API_TOKEN=your_token
```

---

## 🧪 Example Use Cases

* Text generation
* Question answering
* Prompt chaining
* Structured output extraction

---

## 📸 Sample Outputs



---

## 📈 What I Learned

* How LangChain abstracts LLM workflows
* Importance of prompt engineering
* How chaining improves modularity
* Real-world application structure of LLM apps

---

## 🔮 Future Improvements

* Add Retrieval-Augmented Generation (RAG)
* Integrate vector databases (FAISS / Pinecone)
* Build mini AI applications
* Deploy using Streamlit / FastAPI

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!

---

## ⭐ Support

If you find this repository helpful, consider giving it a ⭐ on GitHub!

---

## 📬 Contact

Feel free to connect with me for discussions on AI, ML, and LLMs.

---


