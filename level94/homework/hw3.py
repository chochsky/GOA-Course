import re

def unscrambleEggs(text):
    # This pattern looks for a consonant followed by 'egg' (case insensitive)
    # and replaces it with just the consonant, effectively removing 'egg' after consonants.
    return re.sub(r'([bcdfghjklmnpqrstvwxyz])egg', r'\1', text, flags=re.IGNORECASE)
