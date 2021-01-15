# Дан список целых чисел. Подсчитать сколько четных чисел в списке


my_list = [1, 2, 3, 4, 5, 6]
i = 0
summ = 0
summ2 = 0

while i < len(my_list):
    if my_list[i] % 2 == 0:
        summ += 1
    i += 1

print('колличество четных чисел в списке = ', summ)

for el in my_list:
    if el % 2 == 0:
        summ2 += 1

print('Колличество четных чисел в списке = ', summ2)
