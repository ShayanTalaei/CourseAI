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

    


