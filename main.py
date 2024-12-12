def read_book(path):
    with open(path) as f:
     return f.read()
    
def count_book_words(text):
    all_words = text.split()
    count = 0
    for word in all_words:
       count += 1
    return count

def count_book_chars(text):
    all_words_lowered = text.lower().split()
    word_dict = {}
    for word in all_words_lowered :
       for char in word:
          if char not in word_dict:
             word_dict[char] = 1
          else :
             word_dict[char] += 1
    return word_dict

def print_report(path):
    text = read_book(path)
    count_words = count_book_words(text)
    all_char_dict = count_book_chars(text)

    print(f"--- Begin report of {path} ---")
    print(f"{count_words} words found in the document")
    for char in all_char_dict:
       print(f"The {char} was found {all_char_dict[char]} times")
   

    

def main():
    
    book_path = "books/frankenstein.txt"
    print_report(book_path)
    
main()
