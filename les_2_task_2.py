# codding : utf-8
# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number_user = int(input())
even, odd = 0, 0

while number_user > 0:
    if number_user % 2 == 0:
        even += 1
    else:
        odd += 1
    number_user = number_user // 10

print('четных - ', even, 'нечетных - ', odd)
