from stats import *

def get_book_text(fpath):
    with open(fpath) as f:
        return f.read()
    
def main():
    src_path = "books/frankenstein.txt"
    src_text = get_book_text(src_path)
    num_words = count_words(src_text)
    num_letters = sort_letters(count_letters(src_text))

    print(f"""============ BOOKBOT ============
Analyzing book found at {src_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count ------- """)
    for l in num_letters:
        print(f"{l["char"]}: {l["num"]}")
    
    print("============= END ===============")

main()