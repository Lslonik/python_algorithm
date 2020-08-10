# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

print('Введите две буквы английского алфавита!')
first_letter = input("Введите первую букву: ").lower()
second_letter = input('Введите вторую букву: ').lower()

if 97 <= ord(first_letter) <= 122:
    if 97 <= ord(second_letter) <= 122:
        first_letter_position = ord(first_letter) - 96
        second_letter_position = ord(second_letter) - 96
        print(f"Позиция первой буквы: {first_letter_position}.\nПозиция второй буквы: {second_letter_position}.")
        if ord(first_letter) == ord(second_letter):
            number_of_letters = abs(ord(first_letter) - ord(second_letter))
            print(f"Между буквами {number_of_letters} букв")
        else:
            number_of_letters = abs(ord(first_letter) - ord(second_letter)) - 1
            print(f"Между буквами {number_of_letters} букв")
    else:
        print("Вы ввели не правильные буквы")
else:
    print("Вы ввели не правильные буквы")
