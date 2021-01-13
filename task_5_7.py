# Дана целочисленная квадратная матрица размерности n. Заполнить ее случайными целыми числами. На ти в
# каждо строке наибольши элемент и поменять его местами с элементом главно диагонали.

from random import sample

matrix = []
n = int(input('Введите размер матрицы: '))
m = 0
pos = 0

for i in range(n):
    line = sample(range(0, 100), n)
    matrix.append(line)
print('\n'.join(map(str, matrix)))
for i in matrix:
    for j in i:
        if j == max(i):
            pos = i.index(j)
            head = i[m]
            i[m] = i[pos]
            i[pos] = int(head)
    m += 1

print('\n'.join(map(str, matrix)))