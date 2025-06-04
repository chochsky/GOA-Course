def encode(s):
    # Mapping vowels to numbers
    vowels_to_numbers = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
    # Replace each vowel in the string using the mapping
    return ''.join(vowels_to_numbers.get(ch, ch) for ch in s)

def decode(s):
    # Mapping numbers back to vowels
    numbers_to_vowels = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}
    # Replace each number in the string with its corresponding vowel
    return ''.join(numbers_to_vowels.get(ch, ch) for ch in s)
