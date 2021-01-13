# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь.


leg_1 = 2
leg_2 = 5

hypotenuse = pow(leg_1**2 + leg_2**2, .5)
square = leg_1 * leg_2 / 2

print('Гипотенуза =', hypotenuse)
print('Площадь =', square)