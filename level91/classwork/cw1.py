def convert(text):
    return text.replace('o','u').replace('a','o')
    
def convert(st):
    result=""
    for char in st:
        if char =='a':
            result += 'o'
        elif char == 'o':
            result += 'u'
        else:
            result += char
    return result
        