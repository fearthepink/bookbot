
from stats import (count_words, count_characters, sort_dict_list)


def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)



    path = sys.argv[1]
    book_text = get_book_text(path)
    count = count_words(book_text)
    count_characters(book_text)
    chars = count_characters(book_text)
    da_list = sort_dict_list(chars)
    print_func(path, count, da_list)


def get_book_text(path):
    with open(path, "r") as f:
        book_text = f.read()
        return book_text

def print_func(path, count, da_list):
    print(f"Found {count} total words")
    for item in da_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

main()