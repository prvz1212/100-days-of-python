import random
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score =0
        self.count = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        incorrect_answer = current_question.others
        current_answer = current_question.answer
        option =incorrect_answer
        option.append(current_answer)
        random.shuffle(option)
        self.question_number += 1
        print(f'Q{self.question_number}: {current_question.question} ')
        for i in option:
            self.count += 1
            print(f"Option{self.count}: {i}")
        self.count = 0
        user_answer = input("Choose the answer: ").lower()
        current_answer = current_question.answer
        self.check_answer(user_answer, current_answer)


    def check_answer(self,user_answer, current_answer):
        if user_answer == current_answer.lower():
            self.score += 1
            print(f"You got it right")
        else:
            print(f"Wrong answer")
        print(f"The correct answer was : {current_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n"*2)



    def still_has_question(self):
        return self.question_number < len(self.question_list)


