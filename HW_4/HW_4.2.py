# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».

# Вариант без использования решето
import timeit
import cProfile


def prime(n):
    prime_number = []
    number = 2
    while len(prime_number) < n:
        for j in range(2, number):
            if number % j == 0:
                break
        else:
            prime_number.append(number)
        number += 1
    return prime_number[n - 1]


# print(f'i - е простое число без алгоритма «Решето Эратосфена»: {prime(1000)}')
# print(timeit.timeit('prime(10)', number=1000, globals=globals()))  # 0.016368422999221366
# print(timeit.timeit('prime(20)', number=1000, globals=globals()))  # 0.04566810099640861
# print(timeit.timeit('prime(30)', number=1000, globals=globals()))  # 0.09057647399458801
# print(timeit.timeit('prime(40)', number=1000, globals=globals()))  # 0.14972054200188722
# print(timeit.timeit('prime(50)', number=1000, globals=globals()))  # 0.23970739299693378

cProfile.run('prime(10)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 HW_4.2.py:16(prime)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     29    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('prime(20)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 HW_4.2.py:16(prime)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     71    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     20    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('prime(30)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 HW_4.2.py:16(prime)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#    113    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     30    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Вариант с использованием решето


def def_sieve(n):
    res = []
    number = 2
    while len(res) < n:
        sieve = [i for i in range(number)]
        sieve[0] = 0
        sieve[1] = 0
        for i in range(2, number):
            if sieve[i] != 0:
                j = i + i
                while j < number:
                    sieve[j] = 0
                    j += i
        number += 1
        res = [i for i in sieve if i != 0]
    # print(sieve)
    # print(res)
    return res[-1]


# print(timeit.timeit('def_sieve(10)', number=1000, globals=globals()))  # 0.07356767499732086
# print(timeit.timeit('def_sieve(20)', number=1000, globals=globals()))  # 0.4103548579951166
# print(timeit.timeit('def_sieve(30)', number=1000, globals=globals()))  # 1.035636799999338
# print(timeit.timeit('def_sieve(40)', number=1000, globals=globals()))  # 2.4167771530046593
# print(timeit.timeit('def_sieve(50)', number=1000, globals=globals()))  # 4.197201486000267

# print(f'i - е простое число с помощью алгоритма «Решето Эратосфена»: {def_sieve(1000)}')

cProfile.run('def_sieve(10)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 HW_4.2.py:66(def_sieve)
#    29    0.000    0.000    0.000    0.000 HW_4.2.py:70(<listcomp>)
#    29    0.000    0.000    0.000    0.000 HW_4.2.py:80(<listcomp>)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#    30    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('def_sieve(20)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 HW_4.2.py:66(def_sieve)
#    71    0.000    0.000    0.000    0.000 HW_4.2.py:70(<listcomp>)
#    71    0.000    0.000    0.000    0.000 HW_4.2.py:80(<listcomp>)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#    72    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('def_sieve(30)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#     1    0.001    0.001    0.001    0.001 HW_4.2.py:66(def_sieve)
#   113    0.000    0.000    0.000    0.000 HW_4.2.py:70(<listcomp>)
#   113    0.000    0.000    0.000    0.000 HW_4.2.py:80(<listcomp>)
#     1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#   114    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print('Судя по замерам Эратосфен в моей реализации оказался медленее.')
