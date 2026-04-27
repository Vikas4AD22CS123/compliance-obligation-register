# Compliance Obligation Register (AI Service)

## Overview
This project is a Retrieval-Augmented Generation (RAG) based AI system that answers compliance-related questions using stored documents.

---

## Features
- RAG-based question answering
- ChromaDB for document retrieval
- Groq LLM (llama3-8b)
- Redis-like caching (TTL, hit/miss tracking)
- Health endpoint (/health)
- Meta response (confidence, tokens, latency, cached)

---

## API Endpoints

### POST /query
- Input: question
- Output: answer + sources + meta

### GET /health
- Model info
- Response time
- Cache stats
- Uptime

---

## Testing (Day 10/11)

Tested with 10 different queries.

Initial accuracy was low due to limited data.

After adding definition-based context, system performance improved significantly.

Final average score: **5/5**

---

## Tech Stack
- Python (Flask)
- ChromaDB
- Groq API
- Redis (cache logic)

---

## Key Learning
- Data quality is more important than prompt
- Definition-based context improves retrieval
- Caching improves performance
