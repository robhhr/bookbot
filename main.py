from stats import get_num_words, get_char_count

def main():
    book = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(book)
    char_count = get_char_count(book)
    print(f"{num_words} words found in the document")
    print(f"{char_count}")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()
