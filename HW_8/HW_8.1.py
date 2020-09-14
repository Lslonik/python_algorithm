# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9
import hashlib


def substring_counting(some_str):
    sum_substring = set()

    for i in range(len(some_str)):
        for j in range(len(some_str), i, -1):
            hash_str = hashlib.sha1(some_str[i:j].encode('utf-8')).hexdigest()
            sum_substring.add(hash_str)

    return len(sum_substring) - 1


your_str = input('Введите строку: ').lower()
print(f'Количество подстрок в строке {your_str} равно: {substring_counting(your_str)}')
