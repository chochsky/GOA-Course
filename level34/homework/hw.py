def sum_two_numbers():
    num1 = float(input("შეიტანეთ პირველი რიცხვი: "))
    num2 = float(input("შეიტანეთ მეორე რიცხვი: "))
    print(f"რიცხვების ჯამი არის: {num1 + num2}")
def square_number():
    num = float(input("შეიტანეთ რიცხვი: "))
    print(f"რიცხვის კვადრატი არის: {num ** 2}")
def count_characters():
    name = input("შეიტანეთ თქვენი სახელი: ")
    print(f"სახელის სიმბოლოების რაოდენობა არის: {len(name)}")
def compare_two_numbers():
    num1 = float(input("შეიტანეთ პირველი რიცხვი: "))
    num2 = float(input("შეიტანეთ მეორე რიცხვი: "))
    if num1 > num2:
        print(f"დიდი რიცხვი არის: {num1}")
    elif num2 > num1:
        print(f"დიდი რიცხვი არის: {num2}")
    else:
        print("რიცხვები თანაბარია.")
def check_number():
    num = int(input("შეიტანეთ რიცხვი: "))
    if 1 <= num <= 10:
        print("რიცხვი სწორია.")
    else:
        print("არასწორი რიცხვი.")
def celsius_to_fahrenheit():
    celsius = float(input("შეიტანეთ ტემპერატურა ცელსიუსში: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"ტემპერატურა ფარენჰეიტში არის: {fahrenheit}")
def is_even():
    num = int(input("შეიტანეთ რიცხვი: "))
    return num % 2 == 0
def get_text_length():
    text = input("შეიტანეთ ტექსტი: ")
    return len(text)
