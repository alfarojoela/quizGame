class Question:
    def __init__(self, question_data, question_number):
        self.text = question_data[question_number]["text"]
        self.answer = question_data[question_number]["answer"]



