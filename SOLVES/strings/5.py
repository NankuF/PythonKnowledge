# 5. Дана строка.
# Показать номера символов, совпадающих с последним символом строки.


s = 'impossibles'


def str_index(s: str):
    print(f'last symbol: {s[-1]}')
    for i in range(len(s)):
        if s[i] == s[-1] and i != len(s) - 1:
            print(i, end=' ')


str_index(s)
