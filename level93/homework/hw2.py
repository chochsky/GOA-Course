import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    letters_in_s = set(char.lower() for char in s if char.isalpha())
    return alphabet.issubset(letters_in_s)
