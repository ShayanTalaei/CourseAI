from .exam import *
from .plan import *

class Student:

    def __init__(self, name):
        self.name = name
        self.taken_exams = []
        self.section_to_stats = {}
        self.plan = None

    def take_exam(self, exam, answers, passed_time):
        taken_exam = TakenExam(self, exam, answers, passed_time)
        self.taken_exams.append(taken_exam)

    def update_stats(self, section_to_stats):
        for section, stat in section_to_stats.items():
            if section in self.section_to_stats.keys():
                for key, val in stat:
                    self.section_to_stats[section][key] += key
            else:
                self.section_to_stats[section] = stat

    def get_score_in_section(self, section):
        stats = self.section_to_stats[section]
        corrects = stats["correct_answer"]
        sum_stats = sum([val for key, val in stats.items()])
        return corrects / sum_stats
