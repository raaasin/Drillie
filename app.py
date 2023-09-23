from flask import Flask, render_template, request, jsonify
from qna import pipe
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
            output = pipe.run(
                            query=question, params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}}
                            )
            out=output["answers"][0].answer
            answer = out
            chat_history.append(("Chatbot", answer))
            return jsonify({"answer": answer})
        else:
            answer="I'm sorry I didn't catch that"
            chat_history.append(("Chatbot", answer))
            return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)