
from flask import Flask, render_template, request, jsonify
from rag_engine import (
    get_knowledge_base,
    retrieve_documents,
    generate_answer
)
import time

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    question = str(data.get("question", "")).strip()

    if not question:
        return jsonify({
            "answer": "Please enter a question.",
            "topic": "None",
            "score": 0,
            "response_time_ms": 0
        }), 400

    start = time.perf_counter()

    try:
        knowledge_base = get_knowledge_base()
        results = retrieve_documents(question, knowledge_base)

        if not results:
            return jsonify({
                "answer": (
                    "I can only answer questions related to Operating Systems. "
                    "Please ask an OS-related question."
                ),
                "topic": "None",
                "score": 0,
                "response_time_ms": round(
                    (time.perf_counter() - start) * 1000, 3
                )
            })

        answer = generate_answer(question, results)
        topic = results[0]["topic"]
        score = round(results[0]["score"], 4)

    except Exception:
        app.logger.exception("Error processing question with RAG")
        return jsonify({
            "answer": "Sorry, OSLabAI encountered an error. Please try again.",
            "topic": "Error",
            "score": 0,
            "response_time_ms": round(
                (time.perf_counter() - start) * 1000, 3
            )
        }), 500

    elapsed = (time.perf_counter() - start) * 1000

    return jsonify({
        "answer": answer,
        "topic": topic,
        "score": score,
        "response_time_ms": round(elapsed, 3)
    })


if __name__ == "__main__":
    app.run(debug=True)
