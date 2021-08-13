# 20. Удалить в строке все лишние пробелы,
# то есть серии подряд идущих пробелов заменить на одиночные пробелы.
# Крайние пробелы в строке удалить.

s = '   impossible   my darling  female  '


def cut_space_str(s: str):
    """ Если между словами больше 1 пробела - оставить 1 пробел
        Если пробелов нет - оставить без пробелов
        Если больше 1 пробела - убрать лишние пробелы и оставить 1 пробел"""
    new_s = s.strip()
    n_lst = []
    for i, v in enumerate(new_s):
        if v not in ' ':
            n_lst.append(v)
        elif v in ' ' and new_s[i+1] not in ' ':
            n_lst.append(v)
        else:
            continue

    n_s = ''.join(n_lst)
    n_s = n_s.replace(' ', '_')  # визуальная проверка пробелов
    return n_s


print(cut_space_str(s))
