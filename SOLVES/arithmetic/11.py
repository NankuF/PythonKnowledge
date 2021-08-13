# 11.Вычислите значение выражения
# (|x−5|−sinx)/3+sqrt(x**2+2014)*cos2x−3 при x=−2.34. Ответ: -1.76911 (проверено!)
from math import sin, sqrt, cos

x = -2.34

expr = (abs(x - 5) - sin(x * 3)) / 3 + ((sqrt(x ** 2 + 2014)) * cos(2 * x) - 3)

print(expr)
