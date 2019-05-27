# codding : utf-8
# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

number_user = int(input())
max_summa = 0
max_number = 0

while number_user != 0:
    number_time = number_user
    summa = 0

    while number_user > 0:
        summa += number_user % 10
        number_user //= 10
    if summa > max_summa:
        max_summa = summa
        max_number = number_time

    number_user = int(input())

print('Число', max_number, 'имеет максимальную сумму цифр:', max_summa)