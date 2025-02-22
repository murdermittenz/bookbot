def word_count():
    with open("books/frankenstein.txt") as f:
        words = f.read()
        number_of_words = len(words.split())
        return number_of_words