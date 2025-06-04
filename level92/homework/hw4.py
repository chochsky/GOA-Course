def sort_strings_starting_with_g(strings):
    return sorted(strings, key=lambda s: (not s.lower().startswith('g'), s))
