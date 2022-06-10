from question_model import Question

class QuizBrain:
    
    def __init__(self, questions):
        
        self.question_number = 0
        self.questions: list[Question] = questions
        self.score = 0
        
    def still_has_questions(self):
        
        return self.question_number < len(self.questions)
        
    def next_question(self):
        
        q = self.questions[self.question_number]
        
        q = input(f"Q{self.question_number+1}: {q.question} (true/false): ").lower()
        
        self.check_answer(q)
        
        self.question_number += 1
        
    def check_answer(self, answer):
        
        if answer == self.questions[self.question_number].answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's incorrect")
        print(f"The correct answer was: {self.questions[self.question_number].answer}")
        
        print(f"Your current score is: {self.score}/{self.question_number +1}\n")
        
        
        