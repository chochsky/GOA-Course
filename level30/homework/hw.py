names = ["მარიამი", "გიორგი", "ნინო", "დათო", "თაკო", "ელენე", "ანასტასია", "კოტე", "ლიკა", "ხატია"]
filtered_names = []

for name in names:
    if len(name) <= 10:
        filtered_names.append(name)

print(filtered_names)
numbers = []

for i in range(1, 101):
    numbers.append(i)

print(numbers)
user_input = int(input("შეიტანეთ რიცხვი: "))
user_numbers = []

for i in range(1, user_input + 1):
    user_numbers.append(i)

print(user_numbers)
foods = ["პიცა", "ჰამბურგერი", "სალათი"]
cars = ["BMW", "Mercedes", "Audi"]

combined_list = foods + cars
print(combined_list)
fruits = ["გაბრილ", "ბანანი", "მარწყვი", "საზამთრო", "პამიდორი", "მანდარინი"]
non_fruits = ["პამიდორი", "სტაფილო", "ხახვი"]

for non_fruit in non_fruits:
    if non_fruit in fruits:
        fruits.remove(non_fruit)

print(fruits)
import random

numbers = random.sample(range(1, 101), 20)
even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("ლუწები:", even_numbers)
print("კენტები:", odd_numbers)
