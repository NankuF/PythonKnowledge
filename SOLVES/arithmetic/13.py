# 13. Вычислите значение выражения x2+b−−−−−√5−b2sin3(x+a)x при a=0.1, b=0.2 и x=1 Ответ: 1.0088

from math import sqrt, sin

a = 0.1
b = 0.2
x = 1

f1 = x ** 2 + b
sqrt_stepen = 5
z = pow(f1, (1 / sqrt_stepen))

expr = z - (b ** 2 * sin(x + a) ** 3) / x

print('result:', expr)
print('f1:', f1)
print('z:', z)

# извлечём корень 17-й степени из числа 5600

x = 5600
y = 17
z = pow(x, (1 / y))

print(z)

# проверяем корректность результата
print(pow(z, y))
