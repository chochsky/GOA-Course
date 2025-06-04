def duplicate_encode(word):
    word_lower = word.lower()
    return ''.join('(' if word_lower.count(c) == 1 else ')' for c in word_lower)