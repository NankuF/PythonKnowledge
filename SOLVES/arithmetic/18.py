# 18. Пользователь вводит сторону квадрата.
# Найдите периметр и площадь квадрата.

x = 3


def perimeter_and_area_square(x: int) -> (int, int):
    perimeter = x * 4
    area = x * x
    return perimeter, area,


print(perimeter_and_area_square(x))
