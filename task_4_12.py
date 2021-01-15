# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
# ‘value’}). Чтобы получить список ключей - использовать метод .keys()
# (подсказка: создается новый ключ с цифрой в конце, старый удаляется)

import itertools

dict_1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
i = 0
n1 = list(dict_1.keys())
n2 = list(dict_1.values())

while i < len(n1):
    n1[i] = str(n1[i]) + str(len(n1[i]))
    i += 1
d = list(itertools.zip_longest(n1, n2))
d1 = dict(d)

print(d1)

n1 = list(dict_1.keys())
n2 = list(dict_1.values())
for ind, key in enumerate(dict_1.keys()):
    n1[ind] = str(key) + str(len(key))
d = list(itertools.zip_longest(n1, n2))
d2 = dict(d)

print(d2)
