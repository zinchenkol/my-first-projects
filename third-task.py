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
