# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

your_number = input('Введите натуральное число, или 0 чтобы выйти: ')

number = 0
max_sum = 0
sum_digits = 0


while int(your_number) != 0:
    if your_number == 0:
        break
    if int(your_number) > 0:
        for digit in your_number:
            sum_digits += int(digit)
        if max_sum < sum_digits:
            max_sum = sum_digits
            number = your_number
    else:
        print('Ввели не правильное число!')
    your_number = input('Введите натуральное число, или 0 чтобы выйти: ')
    sum_digits = 0


print(f'Максимальная сумма равна: {max_sum}\nЧисло: {number}')
