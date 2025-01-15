def calculate_word_count_and_sentence_length(text: str):
    word_count = len(text.split())
    sentence_length = len(text.split('.'))  # simple sentence detection by period
    return word_count, sentence_length