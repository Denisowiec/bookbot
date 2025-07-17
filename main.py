from stats import *
import sys

def get_book_text(fpath):
    with open(fpath) as f:
        return f.read()
    
def make_formatted_output(path, words, letters):
    output = f"""============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {words} total words
--------- Character Count ------- """
    for l in letters:
        output += f"\n{l["char"]}: {l["num"]}"
    
    output += "\n============= END ==============="

    return output
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    src_path = sys.argv[1]

    src_text = get_book_text(src_path)
    num_words = count_words(src_text)
    num_letters = sort_letters(count_letters(src_text))
    print(make_formatted_output(src_path, num_words, num_letters))
    

main()