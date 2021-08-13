# 10. Дана строка.
# Если она начинается на 'abc', то заменить их на 'www',
# иначе добавить в конец строки 'zzz'.

s = 'abcxys'


def rename_s(s: str):
    if s[0] == 'a' and s[1] == 'b' and s[2] == 'c':
        new_s = s.replace('abc', 'www', 1)
    else:
        new_s = s + 'zzz'

    return new_s


print(rename_s(s))
