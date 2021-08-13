# 7. Дана строка.
# Определите общее количество символов '+' и '-' в ней.
# А так же сколько таких символов, после которых следует цифра ноль.

s = '+7 (911) 90-50-72'


def check_plus_minus_zero_in_string(s: str):
    storage_plus_minus = []
    storage_before_zero = []
    for i in range(len(s)):
        if s[i] == '+' or s[i] == '-':
            storage_plus_minus.append(1)
        if s[i] == '0':
            storage_before_zero.append(1)

    print('summary "+" and "-": ', len(storage_plus_minus))
    print('summary symbols before "0": ', len(storage_before_zero))


check_plus_minus_zero_in_string(s)
