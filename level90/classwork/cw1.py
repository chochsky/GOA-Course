def is_opposite(s1, s2):
    if not s1 and not s2:
        return False
    if len(s1) != len(s2):
        return False
    for c1, c2 in zip(s1, s2):
        # Letters must be the same ignoring case
        if c1.lower() != c2.lower():
            return False
        # And their cases must be opposite
        if c1.islower() == c2.islower():
            return False
    return True