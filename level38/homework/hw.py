def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

# Example usage:
result = calculator(5, 10, "+")
print("Result:", result)  # Output: Result: 15

def find_max(numbers):
    return max(numbers)

# Example usage:
max_num = find_max([3, 7, 1, 9, 4])
print("Largest number:", max_num)  # Output: Largest number: 9


def find_min(numbers):
    return min(numbers)

# Example usage:
min_num = find_min([3, 7, 1, 9, 4])
print("Smallest number:", min_num)  # Output: Smallest number: 1


def first_letter_position(name):
    first_letter = name[0].lower()
    position = ord(first_letter) - ord('a') + 1
    return position

# User input example:
name = input("Enter your name: ")
position = first_letter_position(name)
print(f"The first letter '{name[0]}' is the {position} letter in the alphabet.")


def greet():
    print("Hello! Welcome!")

# Example usage:
greet()  # Output: Hello! Welcome!
