# Создать строку равную введенно строке без последних двух символов.


string = input('Введите строку: ')

new_string = string[0:len(string) - 2]

print(new_string)