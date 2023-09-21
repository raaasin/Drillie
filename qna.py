from transformers import pipeline
question_answerer = pipeline("question-answering", model='distilbert-base-uncased-distilled-squad')
try:
    with open("data.txt", "r", encoding='utf-8') as file:
        context = file.read()
except UnicodeDecodeError:
    print("Unable to decode the file with UTF-8 encoding. Trying a different encoding...")
    try:
        with open("data.txt", "r", encoding='latin-1') as file:
            context = file.read()
    except Exception as e:
        print(f"Failed to read the file with encoding: {e}")
        context = None  # Handle the error gracefully, e.g., set context to None or an error message.

#print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")