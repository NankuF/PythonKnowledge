# Разработать генератор случайных чисел.
# В функцию передавать начальное и конечное число генерации (нуль необходимо исключить).
# Заполнить этими данными список и словарь.
# Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
# Вывести содержимое созданных списка и словаря.
import random

START = 0
STOP = 15


def random_generator(start: int, stop: int) -> ([], {}):
    if start == 0:
        print('Использовать 0 нельзя, стартовое значение изменено на 1.')
        start = 1
    rand_lst = []
    count = 1
    while count <= stop:
        random_el = random.randrange(start=start, stop=stop)
        rand_lst.append(random_el)
        count += 1

    rand_dict = {}
    for i in rand_lst:
        rand_dict[f'elem_{i}'] = 'value'

    return rand_lst, rand_dict


rand_gen = random_generator(START, STOP)

print('Список случайных чисел:', rand_gen[0], '\nСловарь случайных чисел:', rand_gen[1])
