def get_book_text(fpath):
    with open(fpath) as f:
        return f.read()
    
def main():
    print(get_book_text("books/frankenstein.txt"))

main()