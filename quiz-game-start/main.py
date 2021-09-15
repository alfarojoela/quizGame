from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for index in question_data:
    question_object = Question(index["text"], index["answer"])
    question_bank.append(question_object)

# print(question_bank)
#
# for index in question_bank:
#
#     print(index.text)
#     print(index.answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score} / {quiz.question_number}")
