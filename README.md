# 🎬 CineSage AI

> An AI-powered movie metadata extraction system built while learning Generative AI fundamentals using **LangChain**, **LLMs**, **Prompt Engineering**, **Embeddings**, and **Structured Outputs**.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![LLM](https://img.shields.io/badge/LLM-Generative%20AI-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-blue)

---

# 📖 Overview

CineSage AI is a Generative AI application that converts **unstructured movie-related text** into **structured, machine-readable information** using Large Language Models.

The project demonstrates the practical implementation of modern GenAI concepts such as:

- Large Language Models (LLMs)
- Chat Models
- Prompt Engineering
- Structured Output Parsing
- Embedding Models
- Multiple AI Providers
- Local AI Models
- LangChain Framework

---

# 🎯 Problem Statement

CineSage Analytics is a fictional media intelligence company that receives thousands of movie-related documents every day, including:

- 🎬 Movie Descriptions
- 📰 Press Releases
- ✍️ Blog Articles
- ⭐ Review Summaries
- 🗂 Metadata from Multiple Sources

Unfortunately, this information arrives as long, unstructured paragraphs instead of organized data.

This creates several business challenges:

- ⏳ Manual extraction is time-consuming
- 💰 Processing costs increase rapidly
- ❌ Human errors become common
- 📈 Difficult to scale with growing data

The company needs an automated solution that can understand natural language and generate structured movie metadata.

---

# 💡 Solution

CineSage AI leverages **Large Language Models (LLMs)** with **LangChain** to automatically extract meaningful information from raw movie descriptions.

Instead of manually reading paragraphs, the application produces structured outputs such as:

- 🎥 Movie Title
- 🎭 Genre
- 🎬 Director
- 👥 Cast
- 📅 Release Year
- ⏱ Runtime
- ⭐ Rating (if available)
- 📝 Summary

This makes movie information searchable, reusable, and ready for downstream analytics.

---

# ✨ Features

- 🤖 Chat with Multiple LLM Providers
- 🧠 Prompt Engineering using LangChain
- 📄 Structured Output Generation
- 🔍 Embedding Model Examples
- 🤗 Hugging Face Integration
- 💻 Local Model Support
- 🔐 Secure API Key Management using `.env`
- 📂 Modular Project Structure

---

# 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Framework | LangChain |
| LLM Providers | OpenAI, Groq, Mistral AI, Google Gemini |
| Open Source Models | Hugging Face |
| Environment | Python Virtual Environment |
| Package Manager | pip / uv |
| Secrets Management | python-dotenv |

---

# 📁 Project Structure

```text
Cine-AI/
│
├── chatmodels/
│   ├── chat.py
│   ├── chatbot.py
│   ├── huggingface.py
│   └── uichatbot.py
│
├── cinesage/
│   ├── core.py
│   └── ui_core.py
│
├── embeddingmodels/
│   ├── embeddings.py
│   └── embeddingsopen.py
│
├── assets/
│   ├── chatbot-demo.gif
│   ├── chatbot.png
│   └── architecture.png
│
├── main.py
├── requirements.txt
├── pyproject.toml
├── README.md
├── .gitignore
└── .env.example
```

---

# 🚀 Getting Started

## 1 Clone Repository

```bash
git clone https://github.com/<your-username>/Cine-AI.git

cd Cine-AI
```

---

## 2 Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## 3 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4 Configure Environment Variables

Create a `.env` file.

```env
OPENAI_API_KEY=
GOOGLE_API_KEY=
GROQ_API_KEY=
MISTRAL_API_KEY=
```

---

## 5 Run Project

```bash
python main.py
```

---

# 🧠 Learning Outcomes

Through this project I learned:

- Understanding Large Language Models
- Difference between LLMs and Chat Models
- Working with LangChain
- API Integration
- Prompt Templates
- Prompt Engineering
- Structured Output Parsing
- Embedding Models
- Local AI Models
- Hugging Face Integration
- Secure API Key Management
- Building modular AI applications

---

# 📸 Screenshots

> Add screenshots inside the `assets/` folder.

Example:

```markdown
![Chatbot](assets/chatbot.png)

![Architecture](assets/architecture.png)
```

---

# 🛣 Roadmap

- [x] Chat Models
- [x] Prompt Templates
- [x] Structured Output
- [x] Embeddings
- [x] Hugging Face Integration
- [x] Local Models
- [ ] Retrieval-Augmented Generation (RAG)
- [ ] Vector Databases (FAISS / ChromaDB)
- [ ] Conversation Memory
- [ ] AI Agents
- [ ] Streamlit Deployment
- [ ] Docker Support

---

# 🤝 Acknowledgements

This project was built as part of my **Generative AI learning journey**.

Special thanks to **Akarsh Vyas** for creating an in-depth GenAI tutorial series that inspired and guided the implementation of this project. I have expanded on the concepts by experimenting with different model providers, project organization, and practical implementations.

---

# 📚 Repository Purpose

This repository serves as:

- A portfolio project demonstrating practical Generative AI concepts
- A reference implementation for LangChain fundamentals
- A learning resource documenting my GenAI journey

---

# 👨‍💻 Author

**Tejas Mahajan**

MCA Student | Cloud & Generative AI Enthusiast

Currently exploring:

- Generative AI
- LangChain
- RAG
- AI Agents
- Cloud Computing
- MLOps

---

## ⭐ If you found this project useful, consider giving it a Star!
