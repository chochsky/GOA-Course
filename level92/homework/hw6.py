def expanded_form(num):
    digits = str(num)
    length = len(digits)
    parts = []

    for i, digit in enumerate(digits):
        if digit != '0':
            # Calculate the place value
            place_value = digit + '0' * (length - i - 1)
            parts.append(place_value)
    
    return ' + '.join(parts)
