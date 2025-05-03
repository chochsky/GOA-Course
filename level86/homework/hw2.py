def odd_index_multiples_sum(numbers):
    total = 0
    for i in range(1, len(numbers), 2):  
        total += numbers[i]
    return total


print(odd_index_multiples_sum([1, 2, 3, 4, 5]))  
