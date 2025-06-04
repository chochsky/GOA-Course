import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    letters_in_s = set(char.lower() for char in s if char.isalpha())
    return alphabet.issubset(letters_in_s)
import string

def is_pangram(s):
    s = s.lower()
    alphabet = set(string.ascii_lowercase)
    letters_in_s = set(filter(str.isalpha, s))
    return alphabet.issubset(letters_in_s)
def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
    letters_in_sentence = set(char for char in sentence if char.isalpha())
    return alphabet_set.issubset(letters_in_sentence)