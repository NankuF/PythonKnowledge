# 15. Дана строка.
# Определить, содержит ли строка
# только символы 'a', 'b', 'c' или нет.

s = 'impossible'
s = 'abc'


def is_abc_string(s: str):
    count = 0

    for i in range(len(s)):
        if s[i] == 'a' or s[i] == 'b' or s[i] == 'c':
            count += 1
    if count < len(s):
        return False
    if count == len(s):
        return True
    if count > len(s):
        return 'Ошибка в расчете'


print(is_abc_string(s))
