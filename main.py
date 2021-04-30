from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(entry["text"], entry["answer"]) for entry in question_data]


quiz = QuizBrain(question_bank)
quiz.still_has_questions()
