def sort_words_by_length_desc(sentence):
    words = sentence.split()
    return sorted(words, key=len, reverse=True)
