def get_number_of_words(full_text):
    num_words = full_text.split()
    return len(num_words)

def get_number_of_chars(full_text):
    counter = {}
    lower_text = full_text.lower()
    for char in lower_text:
        counter[char] = counter.get(char, 0) + 1
    return counter

def sort_on(items):
    return items["num"]

