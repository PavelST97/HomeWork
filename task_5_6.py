# Задан целочисленны список c n случайных элементов. Определить количество участков списка,
# на котором элементы монотонно возрастают (каждое следующее число больше предыдущего).

my_array = [1,2,1,1,1,1,14,15]
summ = 0
i = 1

while i < len(my_array) - 1:
    if my_array[i] < my_array[i + 1] and my_array[i] <= my_array[i - 1]:
        summ += 1
    i += 1
if my_array[0] < my_array[1]:
    summ += 1

print(summ)

