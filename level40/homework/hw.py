# solution.py
def basic_op(operation, value1, value2):
    if operation == '+':
        return value1 + value2
    elif operation == '-':
        return value1 - value2
    elif operation == '*':
        return value1 * value2
    elif operation == '/':
        if value2 != 0:
            return value1 / value2
        else:
            return "Error: Division by zero is not allowed"
    else:
        return "Error: Invalid operation"

