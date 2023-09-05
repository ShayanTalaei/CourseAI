
import string
import random

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

class Question:
    
    all_questions = []

    def __init__(self, text, options, correct_option_id, **kwargs):
        self.text = text
        self.options = options
        self.correct_option_id = correct_option_id
        
        self.hardness = kwargs.get("hardness", None)
        self.importance = kwargs.get("importance", None)
        
        self.chapter = kwargs.get("chapter", None)
        self.section = kwargs.get("section", None)
        self.subsection = kwargs.get("subsection", None)
        self.page = kwargs.get("page", None)
        self.tags = kwargs.get("tags", None)

    def check_answer(self, answer):
        return self.correct_option_id == answer

    def generate_random_question():
        text = generate_random_string(length=20)
        options = [generate_random_string(length=5) for i in range(4)]
        correct_option_id = random.randint(0, 4)
        hardness = random.randint(0, 5)
        importance = random.randint(0, 5)

        chapter = 1
        section = random.randint(0, 2)
        subsection = random.randint(0, 1)

        q = Question(
            text, options, correct_option_id, hardness, importance, chapter, section, subsection
        )

        return q

    def choose_random_question(section):
        section_questions = []
        for question in all_questions:
            if question.section == section:
                section_questions.append(question)

        q_count = len(section_questions)
        index = random.randint(0, q_count)
        return section_questions[index]