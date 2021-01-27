# Создать декоратор для функции, которая принимает список чисел. Декоратор должен производить
# предварительную проверку данных - удалять все четные элементы из списка.

def my_decorator(func):
    def wrapper(l1):
        return func([i for i in l1 if i % 2])

    return wrapper


@my_decorator
def my_func(list_1):
    return list_1


if __name__ == '__main__':
    print(my_func([1, 2, 3, 4, 5, 6, 7, 8, 9]))
