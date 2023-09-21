from flask import Flask, render_template, request, jsonify
from qna import question_answerer,context
from judge import classifier

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
        sequence_to_classify = question
        candidate_labels = ['question about mining', 'statement']
        a=classifier(sequence_to_classify, candidate_labels)
        a=a['labels'][0]
        if a=='question about mining':
            result = question_answerer(question=question, context=context)
            answer = result['answer']
            chat_history.append(("Chatbot", answer))
            return jsonify({"answer": answer})
        else:
            answer="I'm sorry I didn't catch that"
            chat_history.append(("Chatbot", answer))
            return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)