# Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 -> 2 3 4 5 1


list_1 = [1, 2, 3, 4, 5]
list_2 = []
i = 1

while i < len(list_1):
    list_2.append(list_1[i])
    i += 1
list_2.append(list_1[0])

print(list_2)

list_2 = []
for el in list_1[1:]:
    list_2.append(el)
list_2.append(list_1[0])

print(list_2)
