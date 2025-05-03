# 19) ასოების დათვლა
user_name = input("შეიყვანეთ სახელი: ")
count = 0
for _ in user_name:
    count += 1
if count == len("ნიკო"):
    print("ერთნაირი რაოდენობის ასოებია.")
else:
    print("კარგი სახელია!")
