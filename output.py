from qna import question_answerer,context
result = question_answerer(question="tell all about minor minerals",     context=context)
print(result['answer'])