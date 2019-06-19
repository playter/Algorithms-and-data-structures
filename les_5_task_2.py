# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как
# [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]

import collections
from collections import deque


hex_irichnoe_dict = collections.defaultdict(list)

# Hex_irichnoe = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
# k = 0
# for i in Hex_irichnoe:
#     hex_irichnoe_dict[k].append(i)
#     k += 1
# print(hex_irichnoe_dict)

# Hex_irichnoe = {0: ['0'], 1: ['1'], 2: ['2'], 3: ['3'], 4: ['4'], 5: ['5'], 6: ['6'], 7: ['7'], 8: ['8'], 9: ['9'], 10: ['A'], 11: ['B'], 12: ['C'], 13: ['D'], 14: ['E'], 15: ['F']}

Hex_irichnoe = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
print(Hex_irichnoe)

a = list(input('Введите первое шестнадцатеричное число, где цифры пишуться с большой буквы: '))
b = list(input('Введите второе шестнадцатеричное число, где цифры пишуться с большой буквы: '))
if len(a) < len(b):
    a, b = b, a
a_pr = a.copy()
b_pr = b.copy()

# m = -1
# p = 0
# summ_and = deque()
# for i in a[::-1]:
#     first_addend = hex_irichnoe_dict.item(i)
#     second_addend = hex_irichnoe_dict.items(b[m])
#     summ_and.append((first_addend + second_addend + p) % 16)
#     if first_addend + second_addend >= 16:
#         p = 1
#     else:
#         p = 0
# print(summ_and)

m = -1
p = 0
summ_and = deque()
for i in a[::-1]:
    first_addend = Hex_irichnoe.index(i)
    second_addend = Hex_irichnoe.index(b[m])
    summ_and.appendleft((first_addend + second_addend + p) % 16)
    if first_addend + second_addend >= 15:
        p = 1
    else:
        p = 0
    m -= 1
    if m == -len(a):
        break
a = a[::-1]
differ = len(a) - len(b)
if differ:
    for i in a[-differ:]:
        summ_and.appendleft(Hex_irichnoe[(Hex_irichnoe.index(a[-differ]) - p) % 16])
        if Hex_irichnoe.index(a[-differ]) + 1 >= 15:
            p = 1
        else:
            p = 0
print(summ_and)
# не смог исправить цифру:15 на букву