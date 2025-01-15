import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from file_utils import load_questions_from_file

def calculate_word_count_and_sentence_length(text: str):
    word_count = len(text.split())
    sentence_length = len(text.split('.'))  # simple sentence detection by period
    return word_count, sentence_length


# cosine similarity between two sets of questions
def compute_cosine_similarity(questions1, questions2):
    all_questions = questions1 + questions2

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_questions)

    cosine_sim = cosine_similarity(tfidf_matrix[:len(questions1)], tfidf_matrix[len(questions1):])
    return cosine_sim


def calculate_diversity(questions):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(questions)

    cosine_sim_matrix = cosine_similarity(tfidf_matrix)

    np.fill_diagonal(cosine_sim_matrix, 0)

    avg_similarity = np.mean(cosine_sim_matrix)

    diversity = 1 - avg_similarity
    return diversity



