# Определить, какое число в массиве встречается чаще всего.

import random
import time
SIZE = int(input('Введите размер массива: '))
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

max_count, arr_el = 0, 0

print(f'Сгенерированный массив: {array}.')

# Вариант 1
start_1 = time.time()

for el in array:
    counter = 0
    for i in range(0, len(array)):
        if el == array[i]:
            counter += 1
            if max_count < counter:
                max_count = counter
                arr_el = el

if max_count == 1:
    print('Повторяющихся элементов нет.')
else:
    print(f'В массиве число = {arr_el} встречается {max_count} раз(а)')

first_var_time = time.time() - start_1


# Вариант 2
start_2 = time.time()

for el in array:
    if array.count(el) > max_count:
        max_count = array.count(el)
        arr_el = el

if max_count == 1:
    print('Повторяющихся элементов нет.')
else:
    print(f'В массиве число = {arr_el} встречается {max_count} раз(а)')

second_var_time = time.time() - start_2


if first_var_time > second_var_time:
    print(f'Второй вариант сработал быстрее!')
else:
    print(f'Первый вариант сработал быстрее!')
