from stats import get_num_words, get_char_count, get_sorted_dictionary_list


def main():
    path = "./books/frankenstein.txt"
    book = get_book_text(path)
    num_words = get_num_words(book)
    char_count = get_char_count(book)
    sorted_dictionary = get_sorted_dictionary_list(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path[2::]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_dictionary:
        is_alpha = i["char"].isalpha()
        if is_alpha:
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


main()
