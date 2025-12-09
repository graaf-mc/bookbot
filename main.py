from stats import get_number_of_words

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_number_of_words(book_text)
    # print("=== Here would have been printed full_book_text ===")
    print(f"Found {num_words} total words")

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
if __name__ == "__main__":
    main()
