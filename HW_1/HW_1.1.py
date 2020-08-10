# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# https://drive.google.com/file/d/1fjcJ49B56SFy05919v0sJDYeQRkis7tc/view?usp=sharing

three_digit_number = int(input("Введите трехзначное число от 100 до 999: "))

if 100 <= three_digit_number < 1000:
    number_1 = three_digit_number // 100
    number_2 = (three_digit_number // 10) % 10
    number_3 = three_digit_number % 10
    print(f"Сумма цифр = {number_1 + number_2 + number_3}")
    print(f"Произведение цифр = {number_1 * number_2 * number_3}")
else:
    print("Вы ввели не трехзначное число!")
