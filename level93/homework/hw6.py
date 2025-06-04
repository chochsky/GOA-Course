def count_zeros(N):
    count = 0
    for num in range(1, N+1):
        count += str(num).count('0')
    return count
