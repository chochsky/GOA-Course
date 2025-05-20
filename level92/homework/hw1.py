def sort_by_vowel_count(lst):
    vowels = "aeiouAEIOU"
    return sorted(lst, key=lambda s: -sum(1 for char in s if char in vowels))
