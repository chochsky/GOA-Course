def most_frequent_count(arr):
    if not arr:
        return 0
    return max(arr.count(x) for x in set(arr))
