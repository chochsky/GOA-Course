def calculate_age(year_of_birth, target_year):
    age = target_year - year_of_birth
    
    if age > 0:
        return f"You are {age} year{'s' if age > 1 else ''} old."
    elif age < 0:
        return f"You will be born in {-age} year{'s' if -age > 1 else ''}."
    else:
        return "You were born this very year!"
