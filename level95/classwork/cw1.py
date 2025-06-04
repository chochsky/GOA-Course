def spin_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # For each word, reverse it if its length is 5 or more
    result = [word[::-1] if len(word) >= 5 else word for word in words]
    
    # Join the words back into a string
    return ' '.join(result)
