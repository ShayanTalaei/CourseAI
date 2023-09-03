from datetime import datetime

class Exam:

    def __init__(self, questions):
        self.question = questions
        self.chapters = [*q.chapters for q in questions if q.chapters != None]


class TakenExam:

    def __init__(self, student, exam, answers, passed_time):
        self.student = student
        self.exam = exam
        self.answers = answers
        self.end_time = datetime.now()
        self.passed_time = passed_time

    def get_score(self):
        return sum([q.check_answer(a) for q, a in zip(self.exam.question, self.answers)])

    
    