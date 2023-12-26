from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    text = i["question"]
    answer = i["correct_answer"]
    objects = Question(text, answer)
    question_bank.append(objects)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_question():
    quiz_brain.next_question()

print("Congratulation. You pass the test quiz")
print(f"Your final score is {quiz_brain.score_number}/{quiz_brain.question_number}")
