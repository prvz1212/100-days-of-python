from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank =[]
for i in question_data:
    question = Question(i["question"],i["correct_answer"], i["incorrect_answers"])
    question_bank.append(question)
# print(question_bank)
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz game")
print(f"Your current score is {quiz.score}/{quiz.question_number}")

