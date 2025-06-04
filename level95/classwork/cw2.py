import re

def solution(s):
    # Insert a space before every uppercase letter
    return re.sub(r'([A-Z])', r' \1', s)
