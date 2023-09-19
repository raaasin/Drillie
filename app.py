from flask import Flask, render_template, request, jsonify
from model import question_answerer,context

app = Flask(__name__)

chat_history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    if request.method == "POST":
        question = request.form["question"]
        chat_history.append(("User", question))
        result = question_answerer(question=question, context=context)
        answer = result['answer']
        chat_history.append(("Chatbot", answer))
        return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)