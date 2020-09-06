import random

m = int(input('Введите натуральное число m: '))
SIZE = 2*m+1
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def search_median(arr):
    for i in range(len(arr)):
        counter_right, counter_left = 0, 0
        for j in range(len(arr)):
            if i != j:
                if arr[i] > arr[j]:
                    counter_left += 1
                elif arr[i] < arr[j]:
                    counter_right += 1
                elif arr[i] == arr[j]:
                    if i < j:
                        counter_right += 1
                    else:
                        counter_left += 1
        # print(f'{arr[i]}, counter_left={counter_left}, counter_right={counter_right}')
        if counter_left == counter_right:
            return f'Медиана массива равна: {arr[i]}. В не отсортированном массиве индекс медианы равен = {i}'

print(array)
print(search_median(array))
