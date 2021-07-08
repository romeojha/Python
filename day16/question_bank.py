from quiz_brain import QuizBrain
from questions import question_data
from main1 import Questions

question_banks = []
for que in question_data:
    que_text = que['text']
    que_ans = que['answer']
    new_que = Questions(qtext=que_text, qanswer=que_ans)
    question_banks.append(new_que)

quiz = QuizBrain(question_banks)
quiz.next_questions()
