from .exam import *

class Student:

    def __init__(self, name):
        self.name = name
        self.taken_exams = []
        

    def take_exam(self, exam, answers, passed_time):
        taken_exam = TakenExam(self, exam, answers, passed_time)
        self.taken_exams.append(taken_exam)

    