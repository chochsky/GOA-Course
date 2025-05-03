def calculator():
    num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
    num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
    operation = input("აირჩიეთ ოპერაცია (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            return "ნულზე გაყოფა არ შეიძლება"
    else:
        return "არასწორი ოპერაცია"

    return f"{num1} {operation} {num2} = {result}"

# მაგალითი გამოძახება:
# print(calculator())
