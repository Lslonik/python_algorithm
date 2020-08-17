# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
# а запрашивает новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

# https://drive.google.com/file/d/1S1v0OjhIOeSggfou2i9KeTuPGNozCaLO/view?usp=sharing

def calculate():
    operation_sign = input("Введите какую хотите выполнить операцию(+,-,*,/) или 0 для выхода: ")
    if operation_sign == '0':
        return "Завершение вычислений"
    elif operation_sign != '+' and operation_sign != '-' and operation_sign != '*' and operation_sign != '/':
        print("Ввели неправильный знак операции")
        return calculate()
    number_1 = int(input("Введите первое число: "))
    number_2 = int(input("Введите второе число: "))
    if operation_sign == '+':
        print(f'Результат сложения равно: {number_1 + number_2}')
        return calculate()
    elif operation_sign == '-':
        print(f'Результат разности равно: {number_1 - number_2}')
        return calculate()
    elif operation_sign == '*':
        print(f'Результат произведения равно: {number_1 * number_2}')
        return calculate()
    else:
        if number_2 == 0:
            print('Деление на 0')
            return calculate()
        else:
            print(f'Результат деления равно: {number_1 / number_2}')
            return calculate()


result = calculate()
print(result)
