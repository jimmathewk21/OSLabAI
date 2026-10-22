# OSLabAI — Operating Systems AI Tutor

## Overview

OSLabAI is a local web-based Operating Systems tutor. It uses Retrieval-Augmented Generation (RAG) to retrieve relevant passages from an Operating Systems knowledge base and generate answers using a locally running language model through Ollama.

## Features

- Interactive chatbot for Operating Systems questions.
- Semantic retrieval using text embeddings and cosine similarity.
- Similarity threshold to reject weakly matching questions.
- Local answer generation using Llama 3.2 3B through Ollama.
- Knowledge base containing 73 passages across Operating Systems topics.
- Dashboard with project overview, implementation details, and runtime metrics.
- Automated tests using pytest.

## Technology Stack

- Python
- Flask
- Ollama
- `nomic-embed-text` for embeddings
- `llama3.2:3b` for answer generation
- NumPy for cosine similarity calculations
- HTML, CSS, and JavaScript
- pytest for automated testing

## Project Files

- `app.py` — Flask web server, chat API, and runtime metrics API.
- `rag_engine.py` — Embedding generation, knowledge-base caching, semantic retrieval, and answer generation.
- `dataset.py` — Operating Systems knowledge-base passages.
- `assistant_logic.py` — Supporting question-answering logic.
- `templates/index.html` — Dashboard and chat interface.
- `static/style.css` — Website styling.
- `static/script.js` — Chat interactions, navigation, and live metrics.
- `test_rag.py` — Interactive manual question-testing script.
- `tests/` — Automated tests.
- `requirements.txt` — Python dependencies.

## Requirements

- Python 3.10 or newer.
- Ollama installed and running locally.
- The following Ollama models:
  - `nomic-embed-text`
  - `llama3.2:3b`

## Setup on Windows

### 1. Open the project folder

Open PowerShell or the VS Code terminal in the OSLabAI project directory.

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, follow your local Python environment policy or activate the environment using the VS Code interpreter selection.

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Install the Ollama models

If the models are not already installed, run:

```powershell
ollama pull nomic-embed-text
ollama pull llama3.2:3b
```

### 5. Start Ollama

Ollama normally runs as a local service on port `11434`. Verify that it responds:

```powershell
Invoke-RestMethod http://localhost:11434/api/tags
```

If Ollama is not running, start it using the appropriate Ollama application or run:

```powershell
ollama serve
```

Do not start a second server if the port is already in use by a running Ollama instance.

### 6. Start OSLabAI

In the project directory, run:

```powershell
python app.py
```

Open the local address printed by Flask, usually:

http://127.0.0.1:5000

## Testing

### Run automated tests

```powershell
python -m pytest -q
```

### Run the interactive RAG test script

```powershell
python test_rag.py
```

Ask an Operating Systems question and inspect the retrieved passages, similarity scores, and generated answer.

## Runtime Metrics

The `/metrics` endpoint reports runtime counters, including total questions, answered questions, rejected questions, failed requests, average response time, and knowledge-base passage count.

These counters are held in memory and reset when the Flask process restarts. They are operational metrics, not measurements of model accuracy.

## Current Limitations

- The knowledge base covers only the Operating Systems material included in the project dataset.
- The similarity threshold is a heuristic. It cannot guarantee that every unrelated question will be rejected or every relevant question accepted.
- Generated answers depend on the retrieved context and the local language model.
- Formal answer accuracy has not been measured using a labelled evaluation dataset.
- Response time depends on the local hardware, model workload, and runtime conditions.
- The prototype is intended for local use and has not been hardened for production deployment.

## Evaluation Status

The current automated test suite has passed 9 tests in the development environment. Manual retrieval checks have also been performed using Operating Systems and unrelated questions.

These results demonstrate basic functionality, not comprehensive correctness or a formal accuracy percentage.
