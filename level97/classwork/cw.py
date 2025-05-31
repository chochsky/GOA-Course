import re

def validate_british_mobile(number):
    if not number:
        return "Plenty more fish in the sea"
    
    # Remove all dashes from the string
    cleaned = number.replace('-', '')
    
    # Define regex patterns for UK mobile numbers:
    # 1) Starts with '07' followed by exactly 9 digits
    pattern_uk = r'^07\d{9}$'
    # 2) Starts with '+44' followed by exactly 9 digits (replacing '0')
    pattern_intl = r'^\+447\d{9}$'
    
    if re.match(pattern_uk, cleaned) or re.match(pattern_intl, cleaned):
        return "In with a chance"
    else:
        return "Plenty more fish in the sea"
