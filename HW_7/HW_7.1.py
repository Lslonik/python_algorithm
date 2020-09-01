import random

SIZE = 7
MIN_ITEM = -100
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for n in range(i):
            if arr[n] > arr[n + 1]:
                arr[n], arr[n + 1] = arr[n + 1], arr[n]


print(f'Исходный массив:\n{array}')
bubble_sort(array)
print(f'Отсортированный массив:\n{array}')
