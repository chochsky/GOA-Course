def generate_hashtag(s):
    # Strip whitespace and split the string into words
    words = s.strip().split()
    
    # Return False if input is empty or no words found
    if not words:
        return False
    
    # Capitalize the first letter of each word and join them
    hashtag = "#" + "".join(word.capitalize() for word in words)
    
    # Check if length exceeds 140 characters
    if len(hashtag) > 140:
        return False
    
    return hashtag
