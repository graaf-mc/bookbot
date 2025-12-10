from stats import get_number_of_words, get_number_of_chars

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_number_of_words(book_text)
    num_chars = get_number_of_chars(book_text)
    # print("=== Here would have been printed full_book_text ===")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print(f"Found the following chars: {num_chars}")
    print("============= END ===============")
    print(num_chars.items())

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
if __name__ == "__main__":
    main()
