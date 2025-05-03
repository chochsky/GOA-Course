def remove_vowels(text):
    vowels = "აეიოუAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result


print(remove_vowels("დავალება"))  
