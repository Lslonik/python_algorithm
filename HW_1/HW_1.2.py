# Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6. В
# ыполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

a = 5
b = 6

print(f'И = {a & b}')
print(f"ИЛИ = {a | b}")
print(f"Отрицание = {~a}, {~b}")
print(f"Исключающее ИЛИ = {a ^ b}")
print(f"Сдвиг вправо на два знака = {a >> 2}")
print(f"Сдвиг влево на два знака = {a << 2}")
