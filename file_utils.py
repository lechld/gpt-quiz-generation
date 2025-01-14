import os
import json
from typing import List
from question import Question

def save_questions(questions: List[Question], filename: str):
    """
    Save a list of Question objects to a JSON file.
    If the file already exists, do not overwrite it but print a warning.
    """
    if os.path.exists(filename):
        print(f"Warning: File '{filename}' already exists. Not overwriting.")
        return

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump([q.to_dict() for q in questions], file, ensure_ascii=False, indent=4)
    print(f"Questions saved to {filename}.")

def load_questions_from_file(filename: str):
    """
    Load questions from a JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return [Question.from_dict(item) for item in data]