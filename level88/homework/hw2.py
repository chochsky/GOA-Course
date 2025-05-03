def is_perfect_square():
    num = int(input("შეიყვანეთ რიცხვი: "))
    root = int(num ** 0.5)
    return root * root == num
