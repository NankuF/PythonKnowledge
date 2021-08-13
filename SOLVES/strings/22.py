# 22. Дан текст.
# Найдите наибольшее количество идущих подряд цифр.
from itertools import count

s = 'He11o my 1i111e fr1end'


def how_many_int_in_text_follow_one_for_one(s: str) -> int:
    # разбиваем строку по словам в лист
    lst = s.split()
    new_s = ''
    # если под индексом только буквы - pass
    # если буквы или буквы-цифры - цифры добавляем в переменную, буквы заменяем на "_"
    for i, v in enumerate(lst):
        if v.isalpha():
            pass
        elif v.isdigit() or v.isalnum():
            for x, y in enumerate(v):
                if y.isdigit():
                    new_s += y
                else:
                    new_s += '_'

    # строку разбиваем по символу '_' и кладем в лист.
    # идем по списку, считаем кол-во идущих подряд цифр, добавляем в новый лист.
    n1 = new_s.split('_')
    n_lst = []
    for i in n1:
        if i.isdigit():
            count = 0
            for _ in i:
                count += 1
                n_lst.append(count)

    # берем максимальное значение из листа = максимум следующих друг за другом цифр
    maximum = max(n_lst)
    # print(maximum)
    # print(n1)
    # print(n_lst)
    return maximum



print(how_many_int_in_text_follow_one_for_one(s))
