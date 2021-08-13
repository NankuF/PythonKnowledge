# 21. Дана строка,
# состоящая из слов, разделенных символами,
# которые перечислены во второй строке.
# Показать все слова.

s = 'love$tree#basic'
s1 = '$#'


def all_words(s: str):
    """Решение работает только для одиночных символов разделяющих слова"""
    lst = s.split()
    n_lst = []
    for i, letter in enumerate(lst):
        for el in letter:
            if el in s1:
                n_lst.append('\n')
            else:
                n_lst.append(el)
    new_s = ''.join(n_lst)
    return new_s


print(all_words(s))
