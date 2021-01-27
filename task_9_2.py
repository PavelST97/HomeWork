# Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по умолчанию 0). Методы:
# увеличить скорости(скорость + 5), уменьшение скорости(скорость - 5), стоп(сброс скорости на 0),
# отображение скорости, разворот(изменение знакаскорости). Все атрибуты приватные.

class Car:
    def __init__(self, brand: str, model: str, year: int, speed: int = 0) -> None:
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed

    def speed_increase(self):
        self.__speed += 5

    def decrease_in_speed(self):
        self.__speed -= 5

    def my_speed(self):
        return self.__speed

    def stop(self):
        self.__speed = 0

    def speed_reversed(self):
        self.__speed = - self.__speed
