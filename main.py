def main():
    book_text = get_text("books/frankenstein.txt")
    number_of_words = words_in_string(book_text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words} words in document\n")
    
    letters_in_string_dictionary = letters_in_string(book_text.lower())
    letters_in_string_list = sort_on(letters_in_string_dictionary)
    for letter in letters_in_string_list:
        if letter[0].isalpha():
            print(f"The '{letter[0]}' character was found {letter[1]} times")
    
    print("--- End report ---")


def get_text(file_path):
    with open(file_path) as datafile:
        return datafile.read()
        
def words_in_string(string):
    return len(string.split())

def letters_in_string(string):
    letters_count_dictionary = {}
    for letter in string:
        if letter in letters_count_dictionary:
            letters_count_dictionary[letter] += 1
        else:
            letters_count_dictionary[letter] = 1
    return letters_count_dictionary

def sort_on(dict):
    return sorted(dict.items(), key=lambda x: x[1], reverse=True)

main()
