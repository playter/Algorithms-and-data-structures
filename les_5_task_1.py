# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple
import collections

enterprises = {}
n = int(input('Введите данные о количестве предприятий: '))
Enterprise = namedtuple('Enterprise', 'enter_name, qu_1, qu_2, qu_3, qu_4')

s = 0
for i in range(n):
    enter_name = tuple(input('Введите наименование предприятия: '))
    g = 0
    list_data_e = []

    for j in range(4):
        gain = int(input(f'прибыль {enter_name} за {j + 1} квартал'))
        list_data_e.append(gain)
        g += gain
        sr_enter_name = g / 4

    enterprise_e = Enterprise(enter_name, list_data_e[0], list_data_e[1], list_data_e[2], list_data_e[3])
    enterprises[enterprise_e.enter_name] = sr_enter_name
    print(sr_enter_name)
    s += g

sr = s / (n * 4)
print(f'Средняя прибыль (за год для всех предприятий)', sr)
print(enterprises)

v_sr = []
n_sr = []
for i in enterprises:
    if enterprises[i] > sr:
        v_sr.append(list(i))

    else:
        n_sr.append(list(i))
print(f'Предприятия, чья прибыль ниже среднего: {n_sr}')
print(f'Предприятия, чья прибыль выше среднего: {v_sr}')


# studs = {}
# n = int(input( "Количество студентов: " ))
# s = 0
# for i in range(n):
#     sname = input(str(i + 1) + "-й студент: ")
#     point = int(input("Балл: "))
#     studs[sname] = point
#     s += point
#
# avrg = s / n
# print( "\nСредний балл: %.0f. Студенты с баллом выше среднего:" % avrg)
# for i in studs:
#     if studs[i] > avrg:
#         print(i)
