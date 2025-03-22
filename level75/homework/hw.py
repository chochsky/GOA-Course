def bonus_time(salary: int, bonus: bool) -> str:
    currency_symbol = "$"  # Python uses "$" as the prefix
    total_salary = salary * 10 if bonus else salary
    return f"{currency_symbol}{total_salary}"

# Example usage:
print(bonus_time(5000, True))  # "$50000"
print(bonus_time(3000, False)) # "$3000"
