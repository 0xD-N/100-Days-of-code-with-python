class Question():
    
    def __init__(self, question:str , answer: str):
        """Initializes question object with a given question and answer"""
        self.question = question
        self.answer = answer.lower()
        
        