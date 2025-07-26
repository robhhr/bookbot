from stats import get_num_words

def main():
    book = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(book)
    print(f"{num_words} words found in the document")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()
