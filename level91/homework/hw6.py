def count_zeros_between_1_and_n(n):
    count = 0
    for i in range(1, n + 1):
        count += str(i).count('0')
    return count
