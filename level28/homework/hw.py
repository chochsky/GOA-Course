for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} არის ლუწი")
    else:
        print(f"{i} არის კენტი")

for i in range(1, 21):
    if i % 3 == 0:
        print(i)

numbers = [3, 7, 12, 5, 18, 2, 9, 15, 20, 1]
for num in numbers:
    if num < 10:
        print(num)

numbers = [8, 15, 3, 22, 6, 4, 10, 1, 9, 18, 12, 5, 2, 7, 14, 11, 20, 17, 19, 0]
for num in numbers:
    if num < 10 and num % 2 == 0:
        print(num)

numbers = [22, 25, 30, 18, 33, 27, 19, 40, 44, 17, 12, 23, 50, 60, 55, 70, 80, 90, 100, 15]
for num in numbers:
    if num > 20 and num % 3 == 0:
        print(num)

names = ["თამარი", "ნიკო", "ანა", "გიო", "კატო"]
for name in names:
    print(f"{name} - {len(name)} ასო")

names = ["თამარი", "ნიკო", "ანა", "გიო", "კატო"]
for name in names:
    print(name[0])

family_members = ["ანა", "გიორგი", "თამარი", "დავით", "მარიამ"]
for member in family_members:
    print(member)

numbers = list(range(1, 11))
print(numbers[0])  # პირველი ელემენტი
print(numbers[-1])  # ბოლო ელემენტი

surname = "პეტრიაშვილი"
for char in surname:
    print(char)

programming_languages = ["Python", "Java", "C++", "JavaScript", "Ruby"]
print(programming_languages)
print(programming_languages[-1])

mixed_list = ["Hello", 42, 3.14, True]
for item in mixed_list:
    print(item)

multiples_of_4 = [i for i in range(0, 21, 4)]
print(max(multiples_of_4))

odd_numbers = [i for i in range(31, 51, 2)]
sum_of_smallest_three = sum(sorted(odd_numbers)[:3])
print(sum_of_smallest_three)
