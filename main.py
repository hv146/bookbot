def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    char_dict = get_chars_dict(text)
    sorted_dict = dict(sorted(char_dict.items(), 
                        reverse=True, 
                        key=lambda x:x[1]))
    get_report(sorted_dict)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_report(char_dict):
    for c in char_dict:
        if c.isalpha() == True:
            print(f"The '{c}' character was found {char_dict[c]}")

    print("--- End report ---")
main()
