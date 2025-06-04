def sort_by_most_vowels(strings):
    vowels = set('aeiouAEIOU')
    return sorted(strings, key=lambda s: sum(ch in vowels for ch in s), reverse=True)
