import random

list = [[random.randint(1,99) for x in range(4)] for y in range(3)]
print("Список >>", list)

s = [sum(row) for row in list]
print(f"Суммы строк: {s}")
print(f"Общая сумма: {sum(s)}")
print(f"строка {s.index(max(s))} макс: {max(s)}")