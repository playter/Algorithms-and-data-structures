
# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 15
MIN_ITEM = 0
MAX_ITEM = 19

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Данный массив создан на основе выбора случайных чисел с помощью random: {array}')

max_num_digits = 1
max_given_number = array[0]

for f_el in range(SIZE - 1):
    num_digits = 1
    for s_el in range(f_el +1, SIZE):
        if array[f_el] == array[s_el]:
            num_digits += 1
        if max_num_digits < num_digits:
            max_num_digits = num_digits
            max_given_number = array[f_el]

print(f'Число {max_given_number} используется для построения массива {max_num_digits} раза')