# Даны три слова. Выяснить, является ли хоть одно из них палиндромом ("перевертышем"), т. е. таким,которое читается
# одинаково слева направо и справа налево. (Определить функцию, позволяющу распознавать слова палиндромы.)

def palindrom(*args):
    for ind in args:
        if ind == ind[::-1]:
            print('True')
            return
        else:
            continue
