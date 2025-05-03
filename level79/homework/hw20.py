# 21) კალკულატორი
operation = input("აირჩიეთ ოპერაცია (+, -, *, /): ")
a = int(input("შეიყვანეთ პირველი რიცხვი: "))
b = int(input("შეიყვანეთ მეორე რიცხვი: "))
if operation == '+':
    print(a + b)
elif operation == '-':
    print(a - b)
elif operation == '*':
    print(a * b)
elif operation == '/':
    print(a / b)
else:
    print("არასწორი ოპერაცია")