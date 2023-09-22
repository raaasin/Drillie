from qna import pipe
from haystack.utils import print_answers
import io
import sys

output_buffer = io.StringIO()
sys.stdout = output_buffer
prediction = pipe.run(
    query="what is mining?", params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}}
)
print_answers(prediction, details="minimal")
sys.stdout = sys.__stdout__
a= output_buffer.getvalue()
print(a)