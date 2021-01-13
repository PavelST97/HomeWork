# Дано число. На ти сумму и произведение его цифр.

number = input('Введите число: ')

summ = 0
comp = 1

for i in number:
    summ += int(i)
    comp *= int(i)

print(summ)
print(comp)
