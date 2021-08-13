# 6. Дана строка.
# Показать третий, шестой, девятый и так далее символы.

s = 'impossibles'
s = 'tooverylongstringeverybodyall'


def str_each_3(s: str):
    len_str = len(s)  # просто захотелось обернуть в переменную
    for i in range(len_str):
        if i % 3 == 0 and i != 0:
            print(f'index: {i}, symbol: {s[i - 1]}')


str_each_3(s)
