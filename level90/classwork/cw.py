from collections import Counter

def duplicate_count(text):
    # Convert to lowercase to make it case-insensitive
    text = text.lower()
    # Count occurrences of each character
    counts = Counter(text)
    # Count how many characters appear more than once
    return sum(1 for char, count in counts.items() if count > 1)
