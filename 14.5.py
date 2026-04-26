N = int(input("Сколько предметов можно унести? "))
items= list(map(int, input("Ценности предметов: ").split()))

items.sort(reverse=True)

# Берем первые N предметов (или все, если их меньше N)
selected_items = items[:N]

# Суммируем только положительные ценности, так как отрицательные брать невыгодно
result = sum(item for item in selected_items if item > 0)

# Выводим результат
print('Максимально возможная суммарная ценность предметов>>: ', result)