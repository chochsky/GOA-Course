def century(year):
    return (year + 99) // 100

# Test cases
print(century(1705))  # Output: 18
print(century(1900))  # Output: 19
print(century(1601))  # Output: 17
print(century(2000))  # Output: 20
print(century(2742))  # Output: 28
