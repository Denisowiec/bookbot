alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

def count_words(s):
    return len(s.split())

def count_letters(s):
    letter_count = {}
    for l in alphabet:
        letter_count[l] = 0

    for l in s:
        if l.lower() in alphabet:
            letter_count[l.lower()] += 1

    return letter_count