def sort_by_fewest_a(strings):
    return sorted(strings, key=lambda s: s.lower().count('a'))
