# codding : utf-8
# Определить, является ли год, который ввел пользователь, високосным или не високосным.

your_year = int(input('Введите год в формате ГГГГ: your_year '))
if your_year % 4 != 0 or (your_year % 100 == 0 and your_year % 400 != 0):
    print("Обычный год")
else:
    print("Високосный год")