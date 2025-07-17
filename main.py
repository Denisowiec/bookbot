from stats import count_words
from stats import count_letters

def get_book_text(fpath):
    with open(fpath) as f:
        return f.read()
    
def main():
    src_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(src_text)
    print(f"{num_words} words found in the document")
    print(count_letters(src_text))

main()