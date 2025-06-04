import string

def is_pangram(s):
    # Convert the string to lowercase
    s = s.lower()
    # Create a set of all letters in the alphabet
    alphabet = set(string.ascii_lowercase)
    # Create a set of letters in the input string
    letters_in_s = set(filter(str.isalpha, s))
    # Check if all letters in the alphabet are in the string
    return alphabet.issubset(letters_in_s)
