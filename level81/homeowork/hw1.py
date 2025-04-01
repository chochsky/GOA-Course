def calculator(a, b, operation):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "unknown value"
    
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b if b != 0 else "unknown value"
    else:
        return "unknown value"

def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"

# Example usage
print(calculator(1, 2, "+"))  # Output: 3
print(calculator(1, 2, "&"))  # Output: "unknown value"
print(calculator(1, "k", "*"))  # Output: "unknown value"

print(people_with_age_drink(13))  # Output: "drink toddy"
print(people_with_age_drink(17))  # Output: "drink coke"
print(people_with_age_drink(18))  # Output: "drink beer"
print(people_with_age_drink(20))  # Output: "drink beer"
print(people_with_age_drink(30))  # Output: "drink whisky"
