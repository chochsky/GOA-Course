def hero(bullets, dragons):
    return bullets >= dragons * 2


print(hero(10, 5))  
print(hero(7, 4))   
print(hero(4, 2))   
print(hero(1, 1))   
print(hero(0, 1))  
