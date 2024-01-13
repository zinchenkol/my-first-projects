# Введення двох чисел
first_number = int(input("Введіть перше число: "))
second_number = int(input("Введіть друге число: "))

# Обробка винятків
if not isinstance(first_number, int) or not isinstance(second_number, int):
    raise TypeError("Введіть два числа")

# Порівняння чисел
if first_number == second_number:
    print("Числа рівні")
else:
    if first_number < second_number:
        print("Перше число менше другого")
    else:
        print("Друге число менше першого")
