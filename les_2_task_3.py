# codding : utf-8
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

number_b = int(input())
number_d = 0

while number_b > 0:
    number_d = number_d*10 + number_b%10
    number_b = number_b//10

print(number_d)