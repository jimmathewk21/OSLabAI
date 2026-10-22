from flask import Flask, render_template, request, jsonify
from rag_engine import (
    get_knowledge_base,
    retrieve_documents,
    generate_answer
)
import time

app = Flask(__name__)

# Runtime metrics: reset whenever the Flask process restarts.
metrics = {
    "total_questions": 0,
    "answered_questions": 0,
    "rejected_questions": 0,
    "failed_requests": 0,
    "total_response_time_ms": 0.0
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/metrics")
def get_metrics():
    knowledge_base = get_knowledge_base()

    total = metrics["total_questions"]
    average_response_time = (
        metrics["total_response_time_ms"] / total
        if total > 0 else 0
    )

    return jsonify({
        **metrics,
        "average_response_time_ms": round(average_response_time, 3),
        "knowledge_base_passages": len(knowledge_base)
    })


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
    metrics["total_questions"] += 1

    try:
        knowledge_base = get_knowledge_base()
        results = retrieve_documents(question, knowledge_base)

        if not results:
            answer = (
                "I can only answer questions related to Operating Systems. "
                "Please ask an OS-related question."
            )

            elapsed = (time.perf_counter() - start) * 1000
            metrics["rejected_questions"] += 1
            metrics["total_response_time_ms"] += elapsed

            return jsonify({
                "answer": answer,
                "topic": "None",
                "score": 0,
                "response_time_ms": round(elapsed, 3)
            })

        answer = generate_answer(question, results)
        topic = results[0]["topic"]
        score = round(results[0]["score"], 4)

        elapsed = (time.perf_counter() - start) * 1000
        metrics["answered_questions"] += 1
        metrics["total_response_time_ms"] += elapsed

        return jsonify({
            "answer": answer,
            "topic": topic,
            "score": score,
            "response_time_ms": round(elapsed, 3)
        })

    except Exception:
        app.logger.exception("Error processing question with RAG")

        elapsed = (time.perf_counter() - start) * 1000
        metrics["failed_requests"] += 1
        metrics["total_response_time_ms"] += elapsed

        return jsonify({
            "answer": "Sorry, OSLabAI encountered an error. Please try again.",
            "topic": "Error",
            "score": 0,
            "response_time_ms": round(elapsed, 3)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
