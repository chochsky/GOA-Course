import math

def dating_range(age):
    if age <= 14:
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)
    else:
        min_age = math.floor(age / 2 + 7)
        max_age = math.floor(2 * (age - 7))
        
    return f"{min_age}-{max_age}"