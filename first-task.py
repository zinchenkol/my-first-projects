# Введення трьох чисел
first_number = float(input("Введіть перше число: "))
second_number = float(input("Введіть друге число: "))
third_number = float(input("Введіть третє число: "))

# Вибір операції
print("Виберіть операцію:")
print("1. Знайти максимум")
print("2. Знайти мінімум")
print("3. Знайти середньоарифметичне")
operation = int(input("Введіть операцію: "))

# Обробка вибору
if operation == 1:
    print("Максимум:", max(first_number, second_number, third_number))
elif operation == 2:
    print("Мінімум:", min(first_number, second_number, third_number))
elif operation == 3:
    print("Середньоарифметичне:", (first_number + second_number + third_number) / 3)
else:
    print("Неправильний вибір операції")
