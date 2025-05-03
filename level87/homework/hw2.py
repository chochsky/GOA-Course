def count_char_occurrences(s: str, char: str) -> int:
    """
    Counts the number of times `char` appears in the string `s`.
    
    :param s: The input string
    :param char: The character to count
    :return: The count of occurrences of `char` in `s`
    """
    if not isinstance(s, str) or not isinstance(char, str) or len(char) != 1:
        raise ValueError("Invalid input: s must be a string and char must be a single character string.")
    
    return s.count(char)


print(count_char_occurrences("hello world", "o"))  