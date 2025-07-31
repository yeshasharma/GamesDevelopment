from question_model import Question

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
    
    def next_question(self):
        score = 0
        for question in self.question_list:
            self.question_number += 1
            answer = input(f"Q. {self.question_number} {question.text} is (True or False)?")
            if answer == question.answer:
                score += 1
            else:
                print(f"Correct answer was: {question.answer}")
        print(f"Your score was {score}")