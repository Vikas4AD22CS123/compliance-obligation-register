\# Compliance Obligation Register (AI Service)



\## Overview

RAG-based system for answering compliance questions.



\## Features

\- ChromaDB retrieval

\- Groq LLM (llama3-8b)

\- Cache (TTL + hit/miss)

\- Health endpoint

\- Meta response

\- Async report generation



\## API



POST /query  

GET /health  

POST /generate-report  

GET /report-status/<job\_id>



\## Testing

10 queries tested → average score: 5/5



\## Day 11

Async processing with background thread + job\_id tracking



\## Tech

Flask, ChromaDB, Groq

