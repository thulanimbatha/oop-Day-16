class QuizBrain:

    question_number = 0
    questions_list = []
    score = 0

    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").lower()
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        '''Returns True if there are still questions left to ask'''
        if self.question_number < len(self.questions_list):
            return True
        return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
