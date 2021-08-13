# 19. Найдите количество вхождения 'aba' в строку.

s = 'abadabadu!!!'


def aba_in_str(s: str):
    new_s = s.count('aba')
    return new_s


def aba_in_str2(s: str):
    return s.count('aba')


print(aba_in_str(s))
print(aba_in_str2(s))
print(type(aba_in_str2(s)))
