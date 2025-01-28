# ხუთის ჯერადი რიცხვების ჯამი (1-დან 100-მდე)
total_sum = 0
for number in range(1, 101):
    if number % 5 == 0:
        total_sum += number

print("ხუთის ჯერადი რიცხვების ჯამი 1-დან 100-მდე:", total_sum)
