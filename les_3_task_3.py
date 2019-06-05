
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

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

array[min_el], array[max_el] = array[max_el], array[min_el]

# _ = array[min_el]
# array[min_el] = array[max_el]
# array[max_el] = _

print(f'Поcле перемещения элементов получаем массив: {array}')