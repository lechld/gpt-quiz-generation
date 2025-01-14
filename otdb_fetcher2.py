from categories import QuestionCategory
from difficulty import Difficulty
from question_type import QuestionType

import requests
import time
import html
from typing import List
from question import Question

class OTDBFetcher:
    BASE_URL = "https://opentdb.com/api.php"
    TOKEN_URL = "https://opentdb.com/api_token.php"
    session_token = None
    max_questions_per_request = 50
    delay_between_requests = 5  # Seconds

    def request_token(self):
        """
        Request a new session token from OTDB.
        """
        response = requests.get(f"{self.TOKEN_URL}?command=request")
        data = response.json()
        if data['response_code'] == 0:
            self.session_token = data['token']
            print(f"Session token obtained: {self.session_token}")
        else:
            raise RuntimeError("Failed to obtain session token.")

    def reset_token(self):
        """
        Reset the session token.
        """
        if self.session_token:
            response = requests.get(f"{self.TOKEN_URL}?command=reset&token={self.session_token}")
            data = response.json()
            if data['response_code'] == 0:
                print("Session token reset successfully.")
            else:
                raise RuntimeError("Failed to reset session token.")
        else:
            raise RuntimeError("No session token available to reset.")

    def get_category_question_count(self, category_id: int) -> int:
        """
        Retrieve the total number of questions available for a category.
        """
        url = f"https://opentdb.com/api_count.php?category={category_id}"
        response = requests.get(url)
        data = response.json()

        if "category_question_count" in data:
            total_questions = data["category_question_count"]["total_question_count"]
            print(f"Total questions available for category {category_id}: {total_questions}")
            return total_questions
        else:
            raise RuntimeError("Failed to retrieve category question count.")

    def fetch_all_questions_in_category(self, category: QuestionCategory, question_type: QuestionType) -> List[Question]:
        """
        Fetch all questions in a category, looping with 50 questions at a time.
        """
        if not self.session_token:
            self.request_token()

        total_questions = self.get_category_question_count(category.otdb_id)
        questions = []
        remaining = total_questions

        while remaining > 0:
            fetch_amount = min(self.max_questions_per_request, remaining)

            url = (
                f"{self.BASE_URL}?amount={fetch_amount}&category={category.otdb_id}"
                f"&token={self.session_token}&qtype={question_type.value}"
            )
            response = requests.get(url)
            data = response.json()

            if data['response_code'] == 0:
                fetched_questions = [
                    Question(
                        question=html.unescape(q['question']),
                        correct_answer=html.unescape(q['correct_answer']),
                        incorrect_answers=[html.unescape(ans) for ans in q['incorrect_answers']],
                        difficulty=q['difficulty']
                    )
                    for q in data['results']
                ]
                questions.extend(fetched_questions)
                remaining -= len(fetched_questions)
                print(f"Fetched {len(fetched_questions)} questions, {remaining} remaining.")
            elif data['response_code'] == 4:  # Token exhausted
                print("Token exhausted. Resetting session token.")
                self.reset_token()
            else:
                print(f"Error fetching questions: {data}")
                raise RuntimeError(f"Failed to fetch questions: {data['response_code']}")

            if remaining > 0:
                print(f"Waiting {self.delay_between_requests} seconds before the next request...")
                time.sleep(self.delay_between_requests)

        print(f"Fetched all {len(questions)} questions for category {category.llm_description}.")
        return questions
