def to_jaden_case(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())
