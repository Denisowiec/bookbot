# alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

def count_words(s):
    return len(s.split())



def count_letters(s):
    letter_count = {}

    for l in s:
        if not l.isalpha():
            continue

        low = l.lower()
        if low in letter_count:
            letter_count[low] += 1
        else:
            letter_count[low] = 1

    return letter_count

def sort_on(items):
    # Helper function to facilitate the sorting of a list of dictionaries.
    return items["num"]

def sort_letters(letters):
    letter_list = []
    for i in letters:
        let_dict = {"char": i, "num": letters[i]} 
        letter_list.append(let_dict)
    
    # Sort the list
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list

