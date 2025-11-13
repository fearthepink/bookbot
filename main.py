from stats import count_words
from stats import count_characters

def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    count_words(book_text)
    count_characters(book_text)
    chars = count_characters(book_text)
    print(chars)


def get_book_text(path):
    with open(path, "r") as f:
        book_text = f.read()
        return book_text


main()