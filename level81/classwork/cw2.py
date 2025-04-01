def count_sheep(sheep):
    
    return sum(1 for s in sheep if s is True)


sheep_array = [
    True, True, True, False, True, True, True, True,
    True, False, True, False, True, False, False, True,
    True, True, True, True, False, False, True, True
]
