# codding : utf-8
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

user_number = input("Введите трехзначное число: ")
user_number = int(user_number)

first_n = user_number % 10
second_n = (user_number % 100) // 10
third_n = user_number // 100

sum = first_n + second_n + third_n
multiplic = first_n * second_n * third_n

print("Сумма цифр числа:", sum)
print("Произведение цифр числа:", multiplic)