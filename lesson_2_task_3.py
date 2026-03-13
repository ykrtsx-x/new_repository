import math


def square(x):
    area = x * x
    if area % 1 != 0:
        area = math.ceil(area)

    return area


area = float(input("Введите сторону квадрата: "))
print("Площадь квадрата: ", square(area))
