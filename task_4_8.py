# Ввести строку. Если длина строки больше 10 символов, то создать новую строку, равную текущей, с
# 3 восклицательными знаками в конце ('!!!') и вывести
# на экран. Если меньше 10, то вывести на экран второй символ строки.


string = input('Введите строку: ')

if len(string) > 10:
    new_string = string + '!!!'
    print(new_string)
else:
    print(string[1])
