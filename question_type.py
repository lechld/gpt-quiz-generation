from enum import Enum

class QuestionType(Enum):
    MULTIPLE_CHOICE = "multiple"
    TRUE_FALSE = "boolean"

    @classmethod
    def get_question_type(cls, name):
        for qtype in cls:
            if qtype.name == name.upper():
                return qtype
        raise ValueError(f"QuestionType {name} not found.")
