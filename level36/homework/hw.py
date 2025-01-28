def sum_two_numbers(a, b):
    return a + b
def is_even(num):
    return num % 2 == 0
def is_greater_than_zero(num):
    return num > 0
def count_elements(my_list):
    return len(my_list)
def min_of_two(a, b):
    return min(a, b)
def square_numbers(numbers):
    return [x ** 2 for x in numbers]
def concatenate_strings(str1, str2):
    return str1 + str2
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def square_number(num):
    return num ** 2
def filter_primes(numbers):
    return [num for num in numbers if is_prime(num)]
def are_equal(a, b):
    return a == b
def first_element(my_list):
    return my_list[0] if my_list else None
