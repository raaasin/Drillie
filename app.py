from flask import Flask, render_template, request, jsonify
from gapi import chatty

dialog_hx = []
app = Flask(__name__)

chat_history = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    if request.method == "POST":
        question = request.form["question"]
        answer = chatty(question)
        return jsonify({"answer": answer})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
