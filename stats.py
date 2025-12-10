def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_number_of_words(full_text):
    num_words = full_text.split()
    return len(num_words)

def get_number_of_chars(full_text):
    counter = {}
    lower_text = full_text.lower()
    for char in lower_text:
        counter[char] = counter.get(char, 0) + 1
    return counter

def sorted_char_num_list(all_chars):
    sorted_list = []
    for chars in all_chars:
        sorted_list.append({"char": chars, "num" :all_chars[chars]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(items):
    return items["num"]

