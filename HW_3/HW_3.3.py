# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = int(input('Введите размер массива: '))
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

min_el, max_el = array[0], array[0]

print(f'Сгенерированный массив: {array}.')

for el in array:
    if min_el > el:
        min_el = el
    if max_el < el:
        max_el = el

index_min_el = array.index(min_el)
index_max_el = array.index(max_el)

array[index_min_el], array[index_max_el] = array[index_max_el], array[index_min_el]

print(f'Минимальный элемент массива: {min_el}.\nМаксимальный элемент массива: {max_el}.\n'
      f'Массив после обмена элементов: {array}')
