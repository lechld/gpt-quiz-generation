from enum import Enum

class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

    @classmethod
    def get_difficulty(cls, name):
        for difficulty in cls:
            if difficulty.name == name.upper():
                return difficulty
        raise ValueError(f"Difficulty {name} not found.")
