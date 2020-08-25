# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
import copy
import timeit
import cProfile


# Вариант 1


def change_min_max(n):
    SIZE = n
    MIN_ITEM = 0
    MAX_ITEM = 10
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

    return print(f'Минимальный элемент массива: {min_el}.\nМаксимальный элемент массива: {max_el}.\n'
                 f'Массив после обмена элементов: {array}')


# print(timeit.timeit('change_min_max(100)', number=1000, globals=globals()))  # 0.07052746300178114
# print(timeit.timeit('change_min_max(200)', number=1000, globals=globals()))  # 0.13417931200092426
# print(timeit.timeit('change_min_max(300)', number=1000, globals=globals()))  # 0.20624839400261408
# print(timeit.timeit('change_min_max(400)', number=1000, globals=globals()))  # 0.28652884400071343
# print(timeit.timeit('change_min_max(500)', number=1000, globals=globals()))  # 0.32676939500379376
# print(timeit.timeit('change_min_max(1000)', number=1000, globals=globals()))  # 0.6626525109968497


cProfile.run('change_min_max(100)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 HW_4.1.py:11(change_min_max)
#     1    0.000    0.000    0.000    0.000 HW_4.1.py:15(<listcomp>)
#   100    0.000    0.000    0.000    0.000 random.py:200(randrange)
#   100    0.000    0.000    0.000    0.000 random.py:244(randint)
#   100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)

cProfile.run('change_min_max(200)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 HW_4.1.py:11(change_min_max)
#     1    0.000    0.000    0.000    0.000 HW_4.1.py:15(<listcomp>)
#   200    0.000    0.000    0.000    0.000 random.py:200(randrange)
#   200    0.000    0.000    0.000    0.000 random.py:244(randint)
#   200    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)

cProfile.run('change_min_max(300)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#     1    0.000    0.000    0.001    0.001 HW_4.1.py:11(change_min_max)
#     1    0.000    0.000    0.000    0.000 HW_4.1.py:15(<listcomp>)
#   300    0.000    0.000    0.000    0.000 random.py:200(randrange)
#   300    0.000    0.000    0.000    0.000 random.py:244(randint)
#   300    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)


# Вариант 2.


def gen_arr(n):
    SIZE = n
    MIN_ITEM = 1
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

    #   print(f'Сгенерированный массив: {array}.')
    return array


def find_max_min(array):
    arr = copy.deepcopy(array)
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr[0], arr[len(arr) - 1]


def change_min_max_loop(n):
    arr = gen_arr(n)
    min_el, max_el = find_max_min(arr)
    index_min_el = arr.index(min_el)
    index_max_el = arr.index(max_el)

    arr[index_min_el], arr[index_max_el] = arr[index_max_el], arr[index_min_el]
    return f'Минимальный элемент массива: {min_el}.\nМаксимальный элемент массива: {max_el}.\n' \
           f'Массив после обмена элементов: {arr}'


# print(timeit.timeit('change_min_max_loop(100)', number=1000, globals=globals()))  # 0.43309687999862945
# print(timeit.timeit('change_min_max_loop(200)', number=1000, globals=globals()))  # 1.4986301610042574
# print(timeit.timeit('change_min_max_loop(300)', number=1000, globals=globals()))  # 3.010785477999889
# print(timeit.timeit('change_min_max_loop(400)', number=1000, globals=globals()))  # 5.123125946003711
# print(timeit.timeit('change_min_max_loop(500)', number=1000, globals=globals()))  # 7.616782965000311
# print(timeit.timeit('change_min_max_loop(1000)', number=1000, globals=globals()))  # 27.75378990000172

cProfile.run('change_min_max_loop(100)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#     1    0.000    0.000    0.001    0.001 HW_4.1.py:108(change_min_max_loop)
#     1    0.000    0.000    0.000    0.000 HW_4.1.py:89(gen_arr)
#     1    0.000    0.000    0.000    0.000 HW_4.1.py:93(<listcomp>)
#     1    0.000    0.000    0.001    0.001 HW_4.1.py:99(find_max_min)
# 101/1    0.000    0.000    0.000    0.000 copy.py:128(deepcopy)
#   100    0.000    0.000    0.000    0.000 copy.py:182(_deepcopy_atomic)
#     1    0.000    0.000    0.000    0.000 copy.py:200(_deepcopy_list)

cProfile.run('change_min_max_loop(200)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 HW_4.1.py:74(gen_arr)
#     1    0.000    0.000    0.000    0.000 HW_4.1.py:78(<listcomp>)
#     1    0.001    0.001    0.002    0.002 HW_4.1.py:84(find_max_min)
#     1    0.000    0.000    0.002    0.002 HW_4.1.py:93(change_min_max_loop)
# 201/1    0.000    0.000    0.000    0.000 copy.py:128(deepcopy)
#   200    0.000    0.000    0.000    0.000 copy.py:182(_deepcopy_atomic)
#     1    0.000    0.000    0.000    0.000 copy.py:200(_deepcopy_list)

cProfile.run('change_min_max_loop(300)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#     1    0.000    0.000    0.001    0.001 HW_4.1.py:74(gen_arr)
#     1    0.000    0.000    0.001    0.001 HW_4.1.py:78(<listcomp>)
#     1    0.003    0.003    0.004    0.004 HW_4.1.py:84(find_max_min)
#     1    0.000    0.000    0.005    0.005 HW_4.1.py:93(change_min_max_loop)
# 301/1    0.000    0.000    0.001    0.001 copy.py:128(deepcopy)
#   300    0.000    0.000    0.000    0.000 copy.py:182(_deepcopy_atomic)
#     1    0.000    0.000    0.001    0.001 copy.py:200(_deepcopy_list)


# Вариант 3
def find_min(arr):
    min_el = 0
    for i in range(len(arr) - 1):
        if arr[min_el] > arr[i]:
            min_el = i
    return min_el


def find_max(arr):
    max_el = 0
    for i in range(len(arr) - 1):
        if arr[max_el] < arr[i]:
            max_el = i
    return max_el


def change_min_max_3(arr, min_el, max_el):
    arr[min_el], arr[max_el] = arr[max_el], arr[min_el]
    return None


def main(n):
    SIZE = n
    MIN_ITEM = 0
    MAX_ITEM = 10
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

    print(f'Сгенерированный массив: {array}.')

    min_el = find_min(array)
    max_el = find_max(array)
    change_min_max_3(array, min_el, max_el)

    return f'Минимальный элемент массива: {array[min_el]}.\nМаксимальный элемент массива: {array[max_el]}.\n' \
           f'Массив после обмена элементов: {array}'


# print(timeit.timeit('main(100)', number=1000, globals=globals()))  # 0.10413638000318315
# print(timeit.timeit('main(200)', number=1000, globals=globals()))  # 0.15789310899708653
# print(timeit.timeit('main(300)', number=1000, globals=globals()))  # 0.2862852530015516
# print(timeit.timeit('main(400)', number=1000, globals=globals()))  # 0.3393328099991777
# print(timeit.timeit('main(500)', number=1000, globals=globals()))  # 0.43247257600160083
# print(timeit.timeit('main(1000)', number=1000, globals=globals()))  # 0.8739276790001895


cProfile.run('main(100)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 HW_4.1.py:146(find_min)
#     1    0.000    0.000    0.000    0.000 HW_4.1.py:154(find_max)
#     1    0.000    0.000    0.000    0.000 HW_4.1.py:162(change_min_max_3)
#     1    0.000    0.000    0.000    0.000 HW_4.1.py:167(main)
#     1    0.000    0.000    0.000    0.000 HW_4.1.py:171(<listcomp>)

cProfile.run('main(200)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 HW_4.1.py:146(find_min)
#     1    0.000    0.000    0.000    0.000 HW_4.1.py:154(find_max)
#     1    0.000    0.000    0.000    0.000 HW_4.1.py:162(change_min_max_3)
#     1    0.000    0.000    0.000    0.000 HW_4.1.py:167(main)
#     1    0.000    0.000    0.000    0.000 HW_4.1.py:171(<listcomp>)
cProfile.run('main(300)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 HW_4.1.py:146(find_min)
#     1    0.000    0.000    0.000    0.000 HW_4.1.py:154(find_max)
#     1    0.000    0.000    0.000    0.000 HW_4.1.py:162(change_min_max_3)
#     1    0.000    0.000    0.000    0.000 HW_4.1.py:167(main)
#     1    0.000    0.000    0.000    0.000 HW_4.1.py:171(<listcomp>)

print('первый вариант обходит второй и третий по скорости')

