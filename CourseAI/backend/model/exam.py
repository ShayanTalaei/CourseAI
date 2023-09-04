from datetime import datetime
import random

from .student import *
from .question import *

class Exam:

    def __init__(self, questions):
        self.questions = questions

    def generate_exam(number_of_questions = 10):
        questions = random.sample(Question.all_questions, number_of_questions)
        return Exam(questions)

    def question_count(self):
        return len(self.questions)

    def get_question_options_list(self, with_answer=False):
        qo_list = []
        for question in self.questions:
            qo_dict = {}
            qo_dict["text"] = question.text
            qo_dict["options"] = question.options
            if with_answer:
                qo_dict["correct_answer"] = question.correct_option_id
            qo_list.append(qo_dict)
        return qo_list

class TakenExam:

    def __init__(self, student, exam, answers, passed_time):
        self.student_name = student.name
        self.exam = exam
        self.answers = answers
        self.end_time = datetime.now()
        self.passed_time = passed_time

    def get_question_options_list(self):
        qo_list = []
        for question, answer in zip(self.exam.questions, self.answers):
            qo_dict = {}
            qo_dict["text"] = question.text
            qo_dict["options"] = question.options
            qo_dict["correct_answer"] = question.correct_option_id
            qo_dict["chosen_answer"] = answer
            qo_dict["chapter"] = question.chapter
            qo_dict["section"] = question.section
            qo_dict["subsection"] = question.subsection
            qo_dict["page"] = question.page
            qo_dict["tags"] = question.tags
            qo_list.append(qo_dict)
        return qo_list

    def get_score(self):
        return sum([q.check_answer(a) for q, a in zip(self.exam.questions, self.answers)])

    
    def calculate_performance_in_sections(self):
        section_to_questions = {}
        for q in self.exam.questions:
            if q.section not in section_to_questions:
                section_to_questions[q.section] = []
            section_to_questions[q.section].append(q)

        
            