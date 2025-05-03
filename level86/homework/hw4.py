def combine_and_sum_evens_odds(list1, list2):
    evens = [x for x in list1 if x % 2 == 0]
    odds = [x for x in list2 if x % 2 != 0]
    combined = evens + odds
    total = sum(combined[i] for i in range(1, len(combined), 2))  
    return total


print(combine_and_sum_evens_odds([2, 4, 5], [1, 3, 6]))  
