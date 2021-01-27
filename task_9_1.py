# Создать три класса, описывающие реальные объекты. Каждый класс должен содержать минимум три
# приватных атрибута, конструктор, геттеры и сеттеры для каждого атрибута, два метода.
import datetime


class Lamp:
    def __init__(self, name: str, power: int, price: int, color: str) -> None:
        self.__name = name
        self.__power = power
        self.__price = price
        self.color = color

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power):
        self.__power = power

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def date(self):
        return datetime.datetime.today().strftime("%d.%m.%Y")

    def time(self):
        return datetime.datetime.today().strftime("%H:%M:%S")


class Book:
    def __init__(self, name, quantity, price, weight):
        self.__name = name
        self.quantity = quantity
        self.__price = price
        self.__weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def string_end(self):
        return 253

    def string_title(self):
        return 9


class Mobile:
    def __init__(self, name, weight, price, color, master):
        self.__name = name
        self.__weight = weight
        self.__price = price
        self.color = color
        self.master = master

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def date_time(self):
        return datetime.datetime.today().strftime("%d.%m.%Y\n%H:%M:%S")

    def inclusion(self):
        return f'Hello {self.master}'
