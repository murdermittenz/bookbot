def word_count(file_path):
    with open(file_path) as f:
        words = f.read()
        number_of_words = len(words.split())
        return number_of_words