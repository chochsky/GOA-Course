def pythagorean_triple(integers):
    # Sort the integers so that the largest number is last
    integers.sort()
    
    # Check if the Pythagorean theorem holds for the sorted integers
    return integers[0]**2 + integers[1]**2 == integers[2]**2
# Example 1
print(pythagorean_triple([5, 3, 4]))  # True (3^2 + 4^2 = 5^2)

# Example 2
print(pythagorean_triple([3, 4, 5]))  # True (3^2 + 4^2 = 5^2)

# Example 3
print(pythagorean_triple([13, 12, 5]))  # True (5^2 + 12^2 = 13^2)

# Example 4
print(pythagorean_triple([100, 3, 999]))  # False (No Pythagorean triple possible)
