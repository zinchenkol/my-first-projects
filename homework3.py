# Завдання 1

# Перелік назв днів тижня
days_of_week = ["понеділок", "вівторок", "середа", "четвер", "п'ятниця", "субота", "неділя"]

# Введення номера дня тижня
day_number = int(input("Введіть номер дня тижня (1-7): "))

# Обробка винятків
if day_number < 1 or day_number > 7:
    raise ValueError("Неправильний номер дня тижня")

# Виведення назви дня тижня
print("День тижня:", days_of_week[day_number - 1])

# Завдання 2

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

# Завдання 3

# Введення двох чисел та математичної дії
first_number = int(input("Введіть перше число: "))
second_number = int(input("Введіть друге число: "))
operation = input("Введіть математичну дію (+, -, * або /): ")

# Обробка винятків
if not operation in "+-*/":
    raise ValueError("Неправильна математична дія")

# Виконання математичної операції
if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
else:
    result = first_number / second_number

# Виведення результату
print("Результат:", result)