# 17. Пользователь вводит три числа.
# Найдите среднее арифметическое этих чисел,
# а также разность удвоенной суммы первого и третьего чисел и утроенного второго числа

x1 = 3
x2 = 4
x3 = 5


def avg_and_diff(x: int, y: int, z: int) -> (float, int):
    average = (x + y + z) / 3
    diff = (x + z) * 2 - x2 * 3
    return average, diff,


print(avg_and_diff(x1, x2, x3))
