# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

I_1 = 2
I_2 = 99
I_3 = 9
numbers = [i for i in range(I_1, I_3 + 1)]
array = [i for i in range(I_1, I_2 + 1)]

print(f'Вот одномерном массив от 2 до 99: {array}')
print(f'Это одномерном массив: {numbers}, для определения кратности')

for delitel in numbers:
    summ_to_i3 = 0
    for number in array:
        if number % delitel == 0:
            summ_to_i3 += 1
    print(f'Из них кратны {delitel} - {summ_to_i3} чисел')