# Создать два списка с различным количеством элементов.
# В первом должны быть записаны ключи, во втором — значения.
# Необходимо написать функцию, создающую из данных ключей и значений словарь.
# Если ключу не хватает значения, в словаре для него должно сохраняться значение None.
# Значения, которым не хватило ключей, необходимо отбросить.


lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
lst2 = [10, 11, 12]

# lst2 = [1, 2, 3, 4, 5, 6, 7, 8]
# lst1 = [10, 11, 12]


def f(key, value):
    dct = {}
    if len(key) > len(value):
        for i, v in enumerate(key):
            if i >= len(value):
                i = None
                dct[v] = i
            else:
                dct[v] = value[i]
    else:
        for i, v in enumerate(key):
            if i >= len(key):
                pass
            else:
                dct[v] = value[i]
    print(dct)


f(lst1, lst2)
