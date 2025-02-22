import sys
from stats import word_count

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def count_chars(text):
    char_counts = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

with open(sys.argv[1]) as f:
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

print(f"--- Begin report of {sys.argv[1]} ---")
print(f"{word_count(sys.argv[1])} words found in the document\n")

for char_dict in char_list:
    print(f"{char_dict['char']}: {char_dict['num']}")

print("--- End report ---")
