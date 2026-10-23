# OSLabAI — Operating Systems AI Tutor

OSLabAI is a local, web-based Operating Systems tutor built using **Retrieval-Augmented Generation (RAG)**. It retrieves relevant passages from an OS knowledge base and uses a local language model to explain concepts.

## Features

- Browser-based chatbot for Operating Systems questions
- Semantic retrieval using embeddings and cosine similarity
- Out-of-scope question rejection using a `0.60` similarity threshold
- Local response generation with Llama 3.2 3B
- Dashboard pages: AI Assistant, Project Overview, Metrics & Testing, Implementation
- Runtime metrics: total, answered, rejected and failed requests, plus average response time
- Automated testing with pytest

## Technology

| Purpose | Tool |
| --- | --- |
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| Model runtime | Ollama |
| Embeddings | `nomic-embed-text` |
| Text generation | `llama3.2:3b` |
| Similarity calculations | NumPy |
| HTTP communication | Requests |
| Tests | pytest |

## RAG Workflow

1. The user submits a question through the web interface.
2. Flask receives the question at `/ask`.
3. `nomic-embed-text` embeds the question.
4. The question embedding is compared with cached embeddings of **73 OS passages** using cosine similarity.
5. If the highest score is below `0.60`, the application rejects the question.
6. Otherwise, up to three passages are included in the prompt to `llama3.2:3b`.
7. The interface displays the answer, source topic, matching score and response time.

The generated embedding cache is stored locally in `knowledge_base.json`. Similarity scores are **not** probabilities of answer correctness.

## Project Structure

```text
OSLabAI/
├── app.py
├── rag_engine.py
├── dataset.py
├── assistant_logic.py
├── test_rag.py
├── tests/
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
├── requirements.txt
└── README.md
```

`app.py` serves the application and APIs; `rag_engine.py` handles embeddings, retrieval, caching and generation; `dataset.py` contains OS passages. `assistant_logic.py` contains supporting/legacy logic.

## Requirements

- Python 3.10+
- Ollama installed and running locally
- Ollama models `nomic-embed-text` and `llama3.2:3b`

## Setup on Windows (PowerShell)

### 1. Clone the repository

```powershell
git clone https://github.com/jimmathewk21/OSLabAI.git
cd OSLabAI
```

If you already have the folder, open it directly in VS Code.

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Install local models

```powershell
ollama pull nomic-embed-text
ollama pull llama3.2:3b
```

### 5. Check Ollama

```powershell
Invoke-RestMethod http://localhost:11434/api/tags
```

If the request fails, open the Ollama application or run `ollama serve` in a separate terminal. If the API responds and `ollama serve` says the port is already in use, the server is already running.

### 6. Start the web app

```powershell
python app.py
```

Open **http://127.0.0.1:5000/** in your browser.

The first run may take longer while the knowledge-base embeddings are generated and cached.

## Example Questions

- Explain paging in an operating system.
- Explain Round Robin CPU scheduling.
- What are the four necessary conditions for deadlock?
- How does virtual memory work?

Unrelated questions, such as asking for a cake recipe or the capital of France, were rejected in manual tests. Rejection is heuristic and not guaranteed for every input.

## Testing

Run the automated tests:

```powershell
python -m pytest -q
```

The development test run reported **9 passed**.

Run the interactive RAG test:

```powershell
python test_rag.py
```

The `/metrics` endpoint returns counters from the current Flask process. They reset when the process restarts.

## Limitations

- The knowledge base contains 73 passages, so coverage is limited.
- The model can produce inaccurate explanations even with relevant context.
- The `0.60` threshold is a heuristic, not a validated classifier.
- Formal answer accuracy has not been measured with a labelled test set.
- Response time depends on the local machine and model workload.
- This is a local prototype, not a production-hardened service.

## Future Work

Expand and review the OS knowledge base; add answer feedback and source previews; build a labelled evaluation dataset; improve performance and error handling; and persist metrics across sessions.

## Authors

- **Vignesh Ekambaram** — 24BCE0651
- **Jim Mathew K** — 24BCE0493

**Course:** BCSE303P — Operating Systems Lab  
**Faculty:** Dr. JAGALINGAM P  
**Institution:** Vellore Institute of Technology, Vellore  
**Academic Year:** 2026–2027

## License

No license has been specified for this repository.
