from dataclasses import dataclass, asdict, field
from typing import List

@dataclass
class Question:
    question: str
    correct_answer: str
    incorrect_answers: List[str] = field(default_factory=list)
    difficulty: str = None

    def to_dict(self):
        """
        Convert the Question object to a dictionary.
        """
        return asdict(self)

    @staticmethod
    def from_dict(data: dict):
        """
        Create a Question object from a dictionary.
        """
        return Question(
            question=data.get('question', ''),
            correct_answer=data.get('correct_answer', ''),
            incorrect_answers=data.get('incorrect_answers', []),
            difficulty=data.get('difficulty', '')
        )