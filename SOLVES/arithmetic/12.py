# 12. Вычислите значение выражения
# e**(x−2)+|sin(x)|−x**4⋅cos*1/x при x=3.6 Ответ: -156.1276
from math import exp, sin, cos

x = 3.6

expr = exp(x - 2) + abs(sin(x)) - x ** 4 * cos(1 / x)

print(expr)
