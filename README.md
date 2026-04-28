# Compliance Obligation Register (AI Service)

## Overview
This project is a Retrieval-Augmented Generation (RAG) based AI system that answers compliance-related questions using stored documents.

---

## Features
- RAG-based question answering
- ChromaDB for document retrieval
- Groq LLM (llama3-8b)
- Response caching (TTL, hit/miss tracking)
- Health monitoring endpoint
- Meta response (confidence, tokens, latency, cache flag)
- Async report generation using background processing

---

## API Endpoints

### POST /query
- Input: question  
- Output: answer + sources + meta  

### GET /health
- Model info  
- Avg response time  
- Cache stats  
- Uptime  

### POST /generate-report
- Returns `job_id` immediately  
- Starts background processing  

### GET /report-status/<job_id>
- Returns job status and result  

---

## Evaluation (Day 10/11)
Tested with 10 different queries.

Initial accuracy was low due to limited data.

After adding definition-based context, system performance improved significantly.

Final average score: **5/5**

---

## Async Processing (Day 11)
Implemented asynchronous report generation:

- Non-blocking API response
- Background thread execution
- Job tracking using `job_id`
- Status endpoint to fetch results

---

## Tech Stack
- Python (Flask)
- ChromaDB
- Groq API
- Redis (for caching logic)

---

## Key Learnings
- Data quality improves retrieval accuracy
- Definition-based context improves answers
- Caching reduces response time
- Async APIs improve system performance