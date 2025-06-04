from collections import Counter

def sort_by_most_threes(numbers):
    count_3 = Counter(numbers)[3]
    return sorted(numbers, key=lambda x: (x != 3, x))
