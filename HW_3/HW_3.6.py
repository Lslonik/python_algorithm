# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать

import random

SIZE = int(input('Введите размер массива: '))
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'Сгенерированный массив: {array}.')

min_el, max_el = array[0], array[0]
min_el_index, max_el_index = 0, 0
my_sum = 0

for el in array:
    if min_el > el:
        min_el = el
        min_el_index = array.index(el)
    if max_el < el:
        max_el = el
        max_el_index = array.index(el)

print(f'Минимальный элемент: {min_el}\nМаксимальный элемент: {max_el}')

if max_el_index - min_el_index < 0:
    for el in range(max_el_index+1, min_el_index):
        my_sum += array[el]
    print(f'Сумма чисел массива между максимальным и минимальным числами {my_sum}')
else:
    for el in range(min_el_index+1, max_el_index):
        my_sum += array[el]
    print(f'Сумма чисел массива между минимальным и максимальным числами {my_sum}')
