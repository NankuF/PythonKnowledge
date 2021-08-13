# 11. Дана строка.
# Если ее длина больше 10, то оставить в строке только первые 6 символов,
# иначе дополнить строку символами 'o' до длины 12.

s = 'impossible'


def cut_upd_string(s: str):
    if len(s) > 10:
        s = s[0:6]
    else:
        while len(s) < 12:
            s += 'o'

    return s


print(cut_upd_string(s))
