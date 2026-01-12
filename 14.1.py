import random

list = [[random.randint(1, 99) for i in range(4)] for j in range(3)]
print ("список", list)

max_n = list [0][0]
r, c = 0, 0
for i in range(3):
    for j in range(4):
        if list[i][j] > max_n:
            max_n, r, c = list[i][j], i, j
print(f"максимум {max_n} в [{r}][{c}]")