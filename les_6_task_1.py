# codding : utf-8
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

from collections import deque
import sys


number_q = input('Введите натуральное число, а я его переверну: ')

# первый вариант
number_b = int(number_q)
number_d = 0
while number_b > 0:
    number_d = number_d*10 + number_b%10
    number_b = number_b//10
print(number_d)


# второй вариант
number_p = deque([i for i in number_q])
number_p.reverse()
print(*number_p, sep='')


# третий вариант
number_d = "".join(number_q[::-1])
print(number_d)


sum_list = [number_q] + [number_b] + [number_p] + [number_d]
sum_keys = ('1', '2', '3', '4')
sum_dict = dict(zip(sum_keys, sum_list))

a = 0

for v_for_sum in sum_dict.values():
    a += sys.getsizeof(v_for_sum)
print(f'Сумма занимаемая в памяти переменными в этих решениях: {a} байт')
# a += sys.getsizeof(v_for_sum) занято памяти 390 байт всеми переменными появляющимися при решении задачи тремя способами

for k_for_sum in sum_dict:
    a += sys.getsizeof(k_for_sum)
print(f'Результирующее значение с учётом ввода ключей к словарю: {a} байт')
# a += sys.getsizeof(k_for_sum) занято памяти 494 байт с учётом ключей словаря