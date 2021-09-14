from data import question_data
from question_model import Question

question_one = Question(question_data, 1)

print(question_one.text)
print(question_one.answer)