from flask import Flask, render_template, request, jsonify
from assistant_logic import answer_question

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

    import time
    start = time.perf_counter()
    answer, topic, score = answer_question(question)
    elapsed = (time.perf_counter() - start) * 1000

    return jsonify({
        "answer": answer,
        "topic": topic,
        "score": score,
        "response_time_ms": round(elapsed, 3)
    })

if __name__ == "__main__":
    app.run(debug=True)
