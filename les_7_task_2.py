# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def merge(left_array, right_array):
    done_array = []
    left_array_id = right_array_id = 0
    left_array_len, right_array_len = len(left_array), len(right_array)

    for _ in range(left_array_len + right_array_len):
        if left_array_id < left_array_len and right_array_id < right_array_len:
            if left_array[left_array_id] <= right_array[right_array_id]:
                done_array.append(left_array[left_array_id])
                left_array_id += 1
            else:
                done_array.append(right_array[right_array_id])
                right_array_id += 1

        elif left_array_id == left_array_len:
            done_array.append(right_array[right_array_id])
            right_array_id += 1

        elif right_array_id == right_array_len:
            done_array.append(left_array[left_array_id])
            left_array_id += 1

    return done_array

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_array = merge_sort(nums[:mid])
    right_array = merge_sort(nums[mid:])
    return merge(left_array, right_array)


SIZE = 7000
MIN_ITEM = 0
MAX_ITEM = 50

array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
array = merge_sort(array)
print(array)