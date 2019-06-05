
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 15
MIN_ITEM = 0
MAX_ITEM = 99

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Данный массив создан с помощью random: {array}')

min_el = 0
max_el = 0
for i in range(SIZE):
    if array[i] < array[min_el]:
        min_el = i
    elif array[i] > array[max_el]:
        max_el = i

if min_el > max_el:
    min_el, max_el = max_el, min_el

summa_otvet = 0
for n in range(min_el + 1, max_el):
    summa_otvet += array[n]
if summa_otvet == 0:
    print(f'Ответ {summa_otvet}, так как элементы стоят рядом это {array[max_el], array[min_el]}')
else:
    print(f'сумму элементов, находящихся между минимальным и максимальным элементами: {summa_otvet}')
# print(array[max_el], max_el, array[min_el], min_el)