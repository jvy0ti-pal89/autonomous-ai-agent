# Autonomous AI Document Agent

## Overview

This project implements an autonomous AI agent using FastAPI and the Groq LLM. The agent accepts a natural language request, generates its own execution plan, performs the required tasks, validates the generated content through a reflection step, and produces a professional Microsoft Word (.docx) document.

The solution demonstrates autonomous planning, task execution, decision-making, document generation, and REST API development without requiring a frontend.

---

## Features

- FastAPI REST API
- POST `/agent` endpoint
- Autonomous execution planning
- Automatic document type detection
- LLM-powered content generation using Groq
- Reflection / Self-check before document generation
- Microsoft Word (.docx) generation
- Professional business document creation

Supported document types include:

- Business Proposal
- Meeting Minutes
- Project Plan
- Business Report
- Technical Design
- Standard Operating Procedure (SOP)

---

## Architecture

```text
User Request
      │
      ▼
Request Validation
      │
      ▼
Planner
(Document Type + Task List)
      │
      ▼
Executor
(LLM Task Execution)
      │
      ▼
Reflection / Self-Check
      │
      ▼
Final Document Generation
      │
      ▼
Microsoft Word (.docx)
```

---

## Tech Stack

- Python
- FastAPI
- Groq API
- python-docx
- Pydantic
- Uvicorn

---

## Project Structure

```text
autonomous-ai-agent/

├── app/
│   ├── agent/
│   │   ├── planner.py
│   │   ├── executor.py
│   │   ├── reflector.py
│   │   └── orchestrator.py
│   │
│   ├── api/
│   ├── llm/
│   ├── models/
│   ├── prompts/
│   ├── tools/
│   └── main.py
│
├── output/
│   └── generated_documents/
│
├── requirements.txt
├── .env
└── README.md
```

---

## Installation

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Run the API

```bash
python -m uvicorn app.main:app --reload
```

Swagger UI

```
http://127.0.0.1:8001/docs
```

---

## API

### POST /agent

Request

```json
{
  "request": "Create a business proposal for implementing an AI-powered CRM."
}
```

Example Response

```json
{
  "status": "completed",
  "document_type": "business_proposal",
  "plan": [
    "Analyze the request",
    "Identify assumptions",
    "Generate document content",
    "Review content",
    "Generate final document"
  ],
  "summary": "Reflection completed successfully.",
  "document_path": "output/generated_documents/business_proposal.docx"
}
```

---

## Engineering Improvement

### Reflection / Self-Check

A reflection stage validates the execution results before generating the final document.

The reflection step checks:

- Task execution completed successfully
- Generated content is available
- The workflow is complete before document generation

This improves reliability by preventing incomplete or empty outputs from being returned to the user.

---

## Example Test Inputs

### Standard Request

```json
{
  "request": "Create a business proposal for implementing an AI-powered CRM system."
}
```

### Complex Request

```json
{
  "request": "Prepare meeting minutes for a client meeting. The attendees are unknown, the budget is not provided, and the timeline should be realistic. Make reasonable assumptions and generate a professional Word document."
}
```

The agent automatically detects missing information, makes reasonable assumptions, generates a professional document, and produces a Microsoft Word file.

---

## Future Improvements

- Conversation Memory
- RAG Integration
- Multi-Agent Architecture
- Tool Calling
- Database Persistence
- Retry and Fallback Logic
- User Authentication
- Cloud Deployment

---

## Author

Jyoti
