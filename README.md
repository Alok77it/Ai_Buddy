# 🤖 AI Buddy

AI Buddy is an intelligent AI-powered assistant built using **Python**, **FastAPI**, and **OpenAI/Gemini APIs**. It helps you explain code, debug errors, auto-generate code, and even integrate with GitHub for project automation.

---

## 🚀 Features

- Code explanation and error debugging
- AI-based code generation
- GitHub integration for automation
- FastAPI backend for seamless API usage

---

## 🛠️ Tech Stack

- Python 3.10+
- FastAPI
- OpenAI or Gemini API
- GitHub REST API

---

## ⚙️ How It Works

1. User sends a query/code via API
2. FastAPI routes it to OpenAI/Gemini
3. AI processes and returns response
4. Optionally pushes to GitHub or displays to user

---

## 📦 Setup

```bash
git clone https://github.com/Alok77it/Ai_Buddy.git
cd Ai_Buddy
pip install -r requirements.txt
uvicorn main:app --reload
```
