# 17. Удалите в строке все буквы 'x'. за которыми следует 'abc'.

s = 'xabc x xabc'


def del_x_before_abc(s: str):
    x = []
    for i in range(len(s)):
        if s[i - 1] == 'x' and s[i] == 'a' and s[i + 1] == 'b' and s[i + 2] == 'c':
            x.append(i - 1)

    new_s = s[x[0] + 1:x[1] - 1] + ' ' + s[x[1] + 1:]
    print(new_s)


del_x_before_abc(s)
