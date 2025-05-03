def is_palindrome():
    word = input("შეიყვანეთ სიტყვა: ")
    reversed_word = ""
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    return word == reversed_word
