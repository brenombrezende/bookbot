def main():
    
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_book_words(text)
    char_dictionary = count_book_letters(text)

    create_char_report(book_path, text, words, char_dictionary)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_book_words(book):
    words = book.split()
    return len(words)

def count_book_letters(text):
    word_dictionary = {}
    text_converted = text.lower()
    for letter in text_converted:
        if letter not in word_dictionary:
            word_dictionary.update({letter:1})
        else:
            word_dictionary[letter] += 1
    return word_dictionary

def create_char_report(path, converted_text, word_count, full_dictionary):
    ordered_list = list(full_dictionary)
    ordered_list = [c for c in ordered_list if c.isalpha()]
    ordered_list.sort()            
   


    print("\n")
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print("\n")
    for l in ordered_list:
        if l in full_dictionary:
            print(f"The {l} character was found {full_dictionary[l]} times")
    print("--- End report ---")
    print("\n")


main()