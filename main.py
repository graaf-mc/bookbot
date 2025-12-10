import sys
from stats import get_book_text, get_number_of_words, get_number_of_chars, sorted_char_num_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_number_of_words(book_text)
    num_chars = get_number_of_chars(book_text)
    report_list = sorted_char_num_list(num_chars)
    # print("=== Here would have been printed full_book_text ===")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in report_list:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")
    
if __name__ == "__main__":
    main()
