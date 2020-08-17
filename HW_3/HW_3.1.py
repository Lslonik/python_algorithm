# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

START_DIGIT = 2
END_DIGIT = 10
START_NUMBER = 2
END_NUMBER = 100

for digit in range(START_DIGIT, END_DIGIT):
    counter = 0
    for number in range(START_NUMBER, END_NUMBER):
        if number % digit == 0:
            counter += 1
    print(f'{counter} чисел кратны {digit} в диапазоне натуральных чисел от 2 до 99.')
