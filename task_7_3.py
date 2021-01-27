# Описать функцию для перевода десятичного числа в двоичное. Описать бесконечный цикл, в котором
# запрашивать у пользователя число и переводить его в двоичную систему. Признак окончания работы
# программы - введенное пользователем число 0. Подсказка: числа в двоичной системе хранить как строки.


def trans(num: int) -> str:
    binary = ''
    while num > 0:
        binary = f'{num % 2}{binary}'
        num = num // 2

    return binary


def result():
    """this function shows the result and checks the number"""
    while True:
        number = int(input('введите число: '))
        if number == 0:
            break
        else:
            print(trans(number))


if __name__ == "__main__":
    result()
