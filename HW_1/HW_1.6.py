# Пользователь вводит номер буквы в алфавите. Определить, какая это буква

letter_number = int(input("Введите номер буквы английского алфавита: "))

if 97 <= ord(chr(96 + letter_number)) <= 122:
    your_letter = chr(96 + letter_number)
    print(f"Ваша буква: {your_letter}")
else:
    print("Такой буквы нет в алфавите")
