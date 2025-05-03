def insert_my_name(name_list):
    my_name = "გიორგი"
    name_list.insert(3, my_name)
    return name_list

# მაგალითი:
names = ["ნინო", "მარიამი", "თემური", "სანდრო", "გოგა"]
print(insert_my_name(names))  # ['ნინო', 'მარიამი', 'თემური', 'გიორგი', 'სანდრო', 'გოგა']
