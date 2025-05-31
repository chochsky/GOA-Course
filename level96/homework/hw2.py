def replace_vowel_codes(arr):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return [chr(num) if chr(num) in vowels else num for num in arr]
