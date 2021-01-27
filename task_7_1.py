# Описать функцию fact2(n), вычисляющую двойной факториал: n!! = 1·3·5·...·n, если n — нечетное; n!! =2·4·6·...·n,
# если n — четное (n > 0 — параметр целоготипа). С помощью это функции найти
# двойные факториалы пяти случайных целых чисел.


def fact2(n):
    fact = 1
    if n % 2:
        for ind in range(1, n+1, 2):
            if ind % 2:
                fact *= ind
        return fact
    else:
        for ind in range(2, n+1, 2):
            if not ind % 2:
                fact *= ind
        return fact


if __name__ == '__main__':
    print((fact2(8)))
