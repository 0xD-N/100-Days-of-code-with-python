from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions = [Question(d["text"], d["answer"]) for d in question_data]

quiz = QuizBrain(questions)

print()
while quiz.still_has_questions():
    quiz.next_question()

print("\nYou completed the quiz.")
print(f"\nYour final score is: {quiz.score}/{quiz.question_number}")