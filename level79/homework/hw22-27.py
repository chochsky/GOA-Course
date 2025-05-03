# 23-27) ლოგიკური ოპერაციების ანალიზი
print(False or True)  # True
print(False and True)  # False
print(False and (True or True))  # False
print((True and False) or True and True or False)  # True
print(False or True and True or False and False or (True and False))  # True
print(True and (True or False) and False or (True and False))  # False
