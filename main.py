import sys
from stats import (
    get_book_text,
    get_number_of_words,
    get_number_of_chars,
    get_chars_dict,
    chars_dict_to_sorted_list
)

def main():
    # if len(sys.argv) != 2:
    #     print("Usage: python3 main.py <path_to_book>")
    #     sys.exit(1)

    book_path = "books/frankenstein.txt"  # sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_number_of_words(book_text)
    # num_chars = get_number_of_chars(book_text)
    # New Lesson added
    chars_dict = get_chars_dict(book_text)
    sorted_list = chars_dict_to_sorted_list(chars_dict)
    # report_list = sorted_char_num_list(num_chars)
    # print("=== Here would have been printed full_book_text ===")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    """
    for char in report_list:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    """
    # New Lesson added
    # Instead off above for loop use:
    sorted_list = chars_dict_to_sorted_list(chars_dict)
    # print(sorted_list)
    # Nicer way:
    for item in sorted_list:
        if item[0].isalpha():
            print(item)
    
    print("============= END ===============")
    
if __name__ == "__main__":
    main()
