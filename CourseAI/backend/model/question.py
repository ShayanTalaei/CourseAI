class Question:
    
    def __init__(self, text, options, correct_option_id, **kwargs):
        self.text = text
        self.options = options
        self.correct_option_id = correct_option_id
        
        self.hardness = kwargs.get("hardness", None)
        self.importance = kwargs.get("importance", None)
        
        self.chapters = kwargs.get("chapters", None)
        self.sections = kwargs.get("sections", None)
        self.subsections = kwargs.get("subsections", None)
        self.pages = kwargs.get("pages", None)
        self.tags = kwargs.get("tags", None)

    def check_answer(self, answer):
        return self.correct_option_id == answer

    


