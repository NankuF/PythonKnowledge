# Изменение размера букв
s = 'hello mister Bob'
# Hello mister bob
print(s.capitalize())  # Пишет строку с Заглавной буквы. Остальные маленькие
# hello mister bob
print(s.lower())  # все с маленькой
# HELLO MISTER BOB
print(s.upper())  # все с большой
# HELLO MISTER bOB
print(s.swapcase())  # меняет размер букв местами
# Hello Mister Bob
print(s.title())  # каждое слово начинается с заглавной

# Проверка строки. Вернет TRUE или FALSE
s = 'abc'
print(s.isalpha())  # только буквы. True
s = '123'
print(s.isdigit())  # только числа. True
s = '12ABc'
print(s.isalnum())  # числа и буквы. True
s = '77'
print(s.isnumeric())  # decimal, digit, numeric. Не содержит float и буквы
s = 'abc12'
print(s.isascii())  # кодировка ascii? True
s = '125634'
print('decimal =', s.isdecimal())  # десятичное число. True
s = 'acids'
print(s.islower())  # вся строка с маленькой буквы. True
s = 'ACIDS'
print('UPPER = ', s.isupper())  # квся строка с большой буквы. True
s = 'Abc Its String'
print(s.istitle())  # каждое слово начинается с заглавной. True
s = 'imidentifier789'
print(s.isidentifier())  # валидный питоний идентификатор. True
s = '   '
print(s.isspace())  # вся строка - это пробелы. True
s = 'its much printable'  # s = '\n \t' - FALSE
print(s.isprintable())  # это можно распечатать. True

# Объединить 2 строки через пробел или иной знак
s1 = 'Hello'
s2 = 'world'
join = ' '.join([s1, s2])  # Hello world
join = '+'.join([s1, s2])  # Hello+world
join = '- '.join([s1, s2])  # Hello- world
join_any = s2.join(s1)  # Hworldeworldlworldlworldo
join_any = s1.join(s2)  # wHellooHellorHellolHellod

# Разделить слова по символу
s1 = 'Hello World'
split_str = s1.split()  # ['Hello', 'World'] тк по дефолту символ == пробел
split_str2 = 'Hello World'.split('+')  # ['Hello World']  тк нет символа +
split_str3 = 'Hello World+gold'.split('+')  # ['Hello World', 'gold']
# rsplit()

# Поиск символа
s = 'Hello my fun'
print(s.index('H'))  # 0 - индекс возвращает ошибку если нет символа.
print(s.find('n'))  # 11 - возвращает -1 если нет символа
# rindex(), rfind()

# Кол-во символов в строке (зависит от регистра)
s = 'oooOoO'
s.count('O')  # 2
s.count('o')  # 4

# Начинается либо заканчивается с символа. Регистрозависимый  (True/False)
s = 'symbol variate'
s.startswith('S')  # False
s.startswith('s')  # True
s.endswith('l')  # False
s.endswith('e')  # True

# Разбить на 3 части по опред.символу
s = 'Hi my name'
print(s.partition('my'))  # ('Hi ', 'my', ' name')
