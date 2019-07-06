# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.

def func(S_str):
    subs_str = set()
    for i in range(len(S_str)):
        for j in range(len(S_str) - 1 if i == 0 else len(S_str), i, -1):
            if hash(S_str[i:j]) not in subs_str:
                subs_str.add(hash(S_str[i:j]))
                # print(S_str[i:j], i, j)
    print(f'Строка "{S_str}" имеет длину {len(S_str)} сиволов. '
          f'Количество неповторяющихся подстрок в этой строке: {len(subs_str)}')


S_str = str(input("Введите строку для посчёта: "))
func(S_str)