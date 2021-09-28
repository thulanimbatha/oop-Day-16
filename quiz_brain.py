class QuizBrain:

    question_number = 0
    questions_list = []

    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text} (True/False): ")

    def still_has_questions(self):
        '''Returns True if there are still questions left to ask'''
        if self.question_number < len(self.questions_list):
            return True
        return False
