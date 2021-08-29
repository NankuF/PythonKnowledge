# Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
# При вызове функции в качестве аргумента должно передаваться имя файла с расширением.
# В функции необходимо реализовать поиск полного пути по имени файла,
# а затем «выделение» из этого пути имени файла (без расширения).

import os

file_name = input('Пожалуйста введите название файла с расширением: ')


def only_name_file(file: str):
    """
    Функция ищет полный путь файла (если они в одной директории), и возвращает название файла без расширения.
    Функция не проверяет, сущесвует ли этот файл в действительности. Просто обрезает расширение и зачем-то
    ищет полный фиктивный путь до директории, в которой запущен этот код.
    """
    not_full_path = os.getcwd()
    full_path = not_full_path + '/' + file
    name_file = os.path.splitext(full_path)
    return name_file[0].split(os.sep)[-1]


print(only_name_file(file_name))