# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
# [-100; 100). Выведите на экран исходный и отсортированный массивы.

import random

def puzir_l(array_1):
    n = 1
    while n < len(array_1):
        for i in range(len(array_1) - 1):
            if array_1[i] > array_1[i + 1]:
                array_1[i], array_1[i + 1] = array_1[i + 1], array_1[i]
        n += 1
    print(array_1)

def puzir_d(array_1):
    for i in range(len(array_1) - 1):
        for j in range((len(array_1) - 1) - i):
            if array_1[j] < array_1[j + 1]:
                array_1[j], array_1[j + 1] = array_1[j + 1], array_1[j]
    print(array_1)

SIZE = 120
MIN_ITEM = -100
MAX_ITEM = 100

array_1 = [random.randrange(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Данный массив создан на основе выбора случайных чисел с помощью random: {array_1}')

puzir_l(array_1) # сортировка на уроке
puzir_d(array_1) # сортировка к дз