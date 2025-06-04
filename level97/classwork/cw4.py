import re

def to_camel_case(text):
    # Split the input by both '-' and '_'
    parts = re.split('[-_]', text)
    
    if not parts:
        return ""
    
    # The first word remains as is (capitalized or not)
    first_word = parts[0]
    
    # Capitalize the first letter of subsequent words
    camel_cased_rest = [word.capitalize() for word in parts[1:]]
    
    # Join everything together
    return first_word + ''.join(camel_cased_rest)
