def alphabet_position(text):
    result = []
    for char in text.lower():
        if char.isalpha():
            # Convert letter to position: 'a' -> 1, 'b' -> 2, ...
            position = ord(char) - ord('a') + 1
            result.append(str(position))
    return ' '.join(result)
