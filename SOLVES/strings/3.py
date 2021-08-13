# 3. Дана строка.
# Вывести первые три символа и последний три символа, если длина строки больше 5.
# Иначе вывести первый символ столько раз, какова длина строки.

s = 'impossible'
low_5 = 'hello'


def string_cut(s: str):
    if len(s) > 5:
        print(s[:3], s[-3:])
    else:
        for i in range(len(s)):
            print(s[0], end='')


string_cut(s)
string_cut(low_5)
