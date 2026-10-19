OSLabAI Website - Local setup

FILES
- app.py: Flask web server and /ask API
- assistant_logic.py: current rule-based question-answering logic
- dataset.py: OS topic documents and keywords
- templates/index.html: dashboard and chat interface
- static/style.css: website styling
- static/script.js: chat interactions and navigation

RUN ON WINDOWS
1. Extract this folder.
2. Open Command Prompt or VS Code terminal in the OSLabAI_Website folder.
3. Optional but recommended:
   python -m venv .venv
   .venv\Scripts\activate
4. Install the dependency:
   pip install -r requirements.txt
5. Start the website:
   python app.py
6. Open the local URL printed in the terminal, usually:
   http://127.0.0.1:5000

IMPORTANT
This is a local prototype. It uses the current rule-based dataset and scoring system. It does not use a trained AI model, TF-IDF, semantic search, or an external API. Those are listed as future improvements only.

The metrics screen records the reported manual test outcomes. It does not claim a formal accuracy percentage. The sample response-time observations are not a benchmark.
