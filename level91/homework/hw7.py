def count_zeros_between_1_and_n(N):
    zero_count = 0
    for num in range(1, N + 1):
        zero_count += str(num).count('0')
    return zero_count
