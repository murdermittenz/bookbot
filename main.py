def word_count():
    with open("books/frankenstein.txt") as f:
        words = f.read()
        number_of_words = len(words.split())
        return number_of_words

def count_chars(text):
    char_counts = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

with open("books/frankenstein.txt") as f:
    text = f.read()
    number_of_characters = count_chars(text)

char_list = []
for char in number_of_characters:
    if char.isalpha():
        new_dict = {"char": char, "num": number_of_characters[char]}
        char_list.append(new_dict)

def sort_on(dict):
    return dict["num"]

char_list.sort(reverse=True, key=sort_on)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count()} words found in the document\n")

for char_dict in char_list:
    print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")

print("--- End report ---")
