# 8. Дана строка.
# Определите, какой символ в ней встречается раньше: 'x' или 'w'.
# Если какого-то из символов нет, вывести сообщение об этом.

s = 'wORx'


def x_or_w(s: str):
    x_index = None
    w_index = None
    for i in enumerate(s):
        if 'x' in i:
            x_index = i[0]
        if 'w' in i:
            w_index = i[0]

    if x_index is None and w_index is None:
        print('x and w is None')
    if x_index is None:
        print('x is none')
        print('w index: ', w_index)
    if w_index is None:
        print('w is none')
        print('x index: ', x_index)
    else:
        if x_index < w_index:
            print('X first')
        else:
            print('W first')


x_or_w(s)
