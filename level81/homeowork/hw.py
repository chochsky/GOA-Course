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

# Example usage
print(calculator(1, 2, "+"))  # Output: 3
print(calculator(1, 2, "&"))  # Output: "unknown value"
print(calculator(1, "k", "*"))  # Output: "unknown value"
