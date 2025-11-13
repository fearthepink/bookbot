def count_words(book_text):
    words = book_text.split()
    counter = 0
    library = []

    for word in words:
        counter += 1
        library.append(word)
    return print(f"Found {counter} total words")


def count_characters(book_text):
        char_count = {}
        for char in book_text.lower():
            char_count[char] = char_count.get(char, 0) + 1
        return char_count

