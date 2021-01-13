# В списке целых случайных чисел с количеством элементов n определить максимальное число и
# заменить им все четные по значению элементы.

first_list = [1, 2, 3, 4, 5, 6, 17]

n = max(first_list)

for i in first_list:
    if i % 2 == 0:
        ind = first_list.index(i)
        first_list.remove(i)
        first_list.insert(ind, n)

print(first_list)
