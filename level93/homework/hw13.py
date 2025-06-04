def expand_string(s):
    if not s:
        return ""

    result = []
    repeat = 1  
    temp_chars = []

    for char in s:
        if char.isdigit():
            repeat = int(char)  
        else:
            temp_chars.append(char)
            
            if len(result) == 0 or not (s[s.index(char)+1:] and s[s.index(char)+1].isdigit()):
                result.extend([c * repeat for c in temp_chars])
                temp_chars = []
                repeat = 1

    if temp_chars:
        result.extend([c * repeat for c in temp_chars])

    return ''.join(result)
