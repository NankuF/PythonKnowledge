# Усовершенствовать первую функцию из предыдущего примера.
# Необходимо во втором списке часть строковых значений заменить на значения типа example345 (строка+число).
# Далее — усовершенствовать вторую функцию из предыдущего примера (функцию извлечения данных).
# Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям:
# вывод первого вхождения, вывод всех вхождений.
# Реализовать замену всех найденных подстрок на новое значение и вывод всех подстрок,
# состоящих из букв и цифр и имеющих пробелы только в начале и конце — например, example345.

# НЕ РЕШЕНО!!

import os


def create_txt(filename: str):
    lst1 = ['hello', 'bob', 'marley', 'is', 'live!']
    lst2 = [1, 2, 3, 'example345', 'example456']
    result = [i + ' ' + str(v) + '\n' for i, v in zip(lst1, lst2)]

    file = str(filename) + '.' + 'txt'
    if os.path.exists(file):
        print('Такой файл уже существует!')

    else:
        with open(file, 'w', encoding='utf-8') as f:
            for i, _ in enumerate(result):
                f.write(result[i])

    pwd = os.getcwd()
    link_file = pwd + '/' + os.path.basename(file)

    def row_print_file():
        with open(link_file, 'r', encoding='utf-8') as f:
            print(f.read())

    row_print_file()


create_txt('my_family')
