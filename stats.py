def count_words(book_text):   
    words = book_text.split()
    counter = 0
    library = []

    for word in words: # can simplify this like crazy with word_count = words.split() /n return len(word_count) and that's it...
        counter += 1
        library.append(word)
    return counter



def count_characters(book_text):# this is much simpler than the example!
        char_count = {}
        for char in book_text.lower():
            char_count[char] = char_count.get(char, 0) + 1
        return char_count

def sort_on(char_count):
    return char_count["num"]

def sort_dict_list(chars):
    sort_list = []
    for key in chars:
        sort_list.append({"char": key, "num": chars[key]})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list

