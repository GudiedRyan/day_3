class QuizBrain:

    def __init__(self, question_bank):
        self.question_list = question_bank
        self.question_number = 0
        self.score = 0
    
    def still_has_questions(self):
        max_questions = len(self.question_list)
        while self.question_number < max_questions:
            self.next_question()
        print("You've compeleted the quiz!")
        print(f"Your final score was {self.score}/{max_questions}\n")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)? \n")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That is incorrect.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")