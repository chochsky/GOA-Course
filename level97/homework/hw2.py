def nickname(name):
    vowels = "aeiou"
    if len(name) < 4:
        return "Error: Name too short"
    
    # Check the 3rd letter (index 2)
    if name[2].lower() in vowels:
        return name[:4]
    else:
        return name[:3]
