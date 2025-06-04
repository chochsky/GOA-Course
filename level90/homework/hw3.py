def is_pangram(sentence):
    # Convert the sentence to lowercase to ignore case
    sentence = sentence.lower()
    
    # Create a set of all alphabet letters
    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
    
    # Create a set of letters found in the sentence
    letters_in_sentence = set(char for char in sentence if char.isalpha())
    
    # Check if the sentence contains all letters in the alphabet
    return alphabet_set.issubset(letters_in_sentence)
