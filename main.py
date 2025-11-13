def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    count_words(book_text)


def get_book_text(path):
    with open(path, "r") as f:
        book_text = f.read()
        return book_text
   
def count_words(book_text):
    words = book_text.split()
    counter = 0
    library = []

    for word in words:
        counter += 1
        library.append(word)
    return print(f"Found {counter} total words")

        



main()