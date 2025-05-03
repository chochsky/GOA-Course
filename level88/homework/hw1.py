def divide_by_digit_sum():
    num = int(input("შეიყვანეთ რიცხვი: "))
    digit_sum = sum(int(digit) for digit in str(num))
    if digit_sum == 0:
        return
    return num / digit_sum
