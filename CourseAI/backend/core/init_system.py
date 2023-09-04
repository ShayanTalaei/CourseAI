from model.student import *
from model.question import *

def initialize_system():
    student = Student("شایان")
    # load questions into all questions
    
    Question.all_questions = [Question.generate_random_question() for _ in range(100)]

    return student