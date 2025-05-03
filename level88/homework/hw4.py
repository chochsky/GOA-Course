def hide_vowels():
    word = input("შეიყვანეთ სიტყვა: ")
    vowels = "aeiouAEIOUაეიოუ"
    result = ''.join(['*' if char in vowels else char for char in word])
    return result
