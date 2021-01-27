# Создать универсальны декоратор, которы меняет порядок аргументов в функции на противоположны .

def my_decorator(func):
    def wrapper(*args):
        return func(*args[::-1])

    return wrapper


@my_decorator
def my_func(*args):
    return args


if __name__ == '__main__':
    print(my_func([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 3))
