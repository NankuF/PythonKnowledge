# 14. Пользователь вводит два числа.
# Найдите сумму и произведение данных чисел.

x = 5
y = 2


def sum_and_mul(x: int, y: int) -> (int, int):
    summary = x + y
    mul = x * y
    return summary, mul


print(sum_and_mul(x, y))
