import requests
import html

from categories import QuestionCategory
from difficulty import Difficulty
from question_type import QuestionType

def fetch_otdb_questions(amount, category: QuestionCategory, difficulty: Difficulty, qtype: QuestionType):
    """
    Fetch questions from OTDB API based on category, difficulty, and question type.
    """
    url = f"https://opentdb.com/api.php?amount={amount}&category={category.otdb_id}&difficulty={difficulty.value}&type={qtype.value}"
    response = requests.get(url)
    data = response.json()

    if data['response_code'] == 0:
        return data['results']  # Returns a list of questions
    else:
        raise RuntimeError("Failed to fetch questions from OTDB.")

def print_questions(questions):
    """
    Print the fetched questions in a readable format.
    """
    for idx, question in enumerate(questions, start=1):
        question_text = html.unescape(question['question'])
        correct_answer = html.unescape(question['correct_answer'])
        incorrect_answers = [html.unescape(ans) for ans in question['incorrect_answers']]

        print(f"Question {idx}: {question_text}")
        if incorrect_answers and correct_answer:
            answers = incorrect_answers + [correct_answer]
            for i, answer in enumerate(sorted(answers), start=1):
                print(f"  {i}. {answer}")
        print(f"Correct Answer: {correct_answer}")
        print("-" * 50)