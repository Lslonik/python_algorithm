# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


your_number = input("Введите натуральное число: ")

if int(your_number) > 0:
    odd_number = 0
    even_number = 0
    for i in your_number:
        if int(i) % 2 == 0:
            even_number += 1
        else:
            odd_number += 1
    print(f'Ваше число = {your_number}\nЧетные цифры в числе = {even_number}\nНечетные цифры в числе = {odd_number}')
else:
    print('Ввели не натуральное число')
