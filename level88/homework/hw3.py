def most_frequent_number(lst):
    from collections import Counter
    count = Counter(lst)
    return count.most_common(1)[0][0]  
