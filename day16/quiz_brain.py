from question_bank import question_banks


class QuizBrain:

    def __init__(self, question_list):
        question_no = 0
        self.question_list = question_list

    def next_question(self):
        current_question=self.question_list[self.question_no]
        input(f'Q.{self.question_no}:{current_question.text}true or false')
