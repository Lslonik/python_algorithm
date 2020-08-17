# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более
# чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то,
# что загадано.
# Если за 10 попыток число не отгадано, вывести правильный ответ

from random import randint

number = randint(0, 100)
i = 0

while i < 10:
    your_number = int(input("Отгадайте число от 0 до 100: "))
    if 0 < your_number < 100:
        if your_number == number:
            print(f'Поздравляю вы угадали число. Использовали {i + 1} попыток')
            break
        else:
            if your_number < number:
                print('Загаданное число больше чем ваше')
                i += 1
            else:
                print('Загаданное число меньше чем ваше')
                i += 1
    else:
        print('Ввели некорректное число!')
        i += 1
else:
    print('Вы проиграли')
