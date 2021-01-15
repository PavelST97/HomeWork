# Составить список чисел Фибоначчи содержащий 15 элементов.
# (Подсказка: Числа Фибоначчи - последовательность, в которой первые два числа равны
# либо 1 и 1, а каждое последующее число равно сумме двух предыдущих чисел.
# Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34...


fibonachi = [1, 1]
n = 13
i = 0

while i < n:
    fibonachi.append(fibonachi[i] + fibonachi[i + 1])
    i += 1

print(fibonachi)

fibonachi = [1, 1]

for el in range(0, 13):
    fibonachi.append(fibonachi[el] + fibonachi[el + 1])

print(fibonachi)
