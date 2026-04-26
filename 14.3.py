list1 = [[10, -5, 0, 8], [-3, 7, -1, 4], [0, -2, 6]]
filtered = []

for sublist in list1:
    temp = []
    for num in sublist:
        if num > 0:
            temp.append(num)
    filtered.append(temp)

print("Исходный:", list1)
print("Отфильтрованный:", filtered)