# Дан список целых чисел.
# Создать новый список, каждый элемент которого равен исходному элементу умноженному на -2


my_list = [1, 2, 3, 4, 5]
my_new_list = []

i = 0
while i < len(my_list):
    my_new_list.append(my_list[i] * -2)
    i += 1

print(my_new_list)

my_new_list2 = []

for el in list_1:
    my_new_list2.append(el*-2)

print(my_new_list2)
