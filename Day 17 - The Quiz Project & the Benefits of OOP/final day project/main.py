from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#generate questions from question_data
questions = [Question(d["text"], d["answer"]) for d in question_data]

#generate quiz object and initialize it with a list of question objects
quiz = QuizBrain(questions)


print()

# continue the quiz while questions remain
while quiz.still_has_questions():
    quiz.next_question()

#show results to user
print("\nYou completed the quiz.")
print(f"\nYour final score is: {quiz.score}/{quiz.question_number}")