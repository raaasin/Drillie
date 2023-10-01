from flask import Flask, render_template, request, jsonify
"""
from models.roberta import pipe
from models.bart import classifier
from models.pGPT import tokenizer,generate_next,to_var,personas,flatten
"""

dialog_hx=[]
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
        """
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
            
            user_inp = tokenizer.encode(">> User: "+ question + tokenizer.eos_token)
            dialog_hx.append(user_inp)
            bot_input_ids = to_var([personas + flatten(dialog_hx)]).long()
            msg = generate_next(bot_input_ids)
            dialog_hx.append(msg)
            answer="{}".format(tokenizer.decode(msg, skip_special_tokens=True))
            chat_history.append(("Chatbot", answer))
            return jsonify({"answer": answer})
        """
        chat_history.append(("Chatbot","Example reply Example reply Example reply Example reply Example reply Example replyExample replyExample replyExample replyExample replyExample replyExample replyExample replyExample replyExample reply"))
        return jsonify({"answer": "Example reply Example reply Example reply Example reply Example reply Example replyExample replyExample replyExample replyExample replyExample replyExample replyExample replyExample replyExample reply"})

        
if __name__ == "__main__":
    app.run(debug=True)