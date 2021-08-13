# 1 Дана строка. Вывести ее три раза через запятую и показать количество символов в ней.
s = 'My name is Valeriy'
lens = 0
for i in range(3):
    if i < 2:
        print(s + ', ', end='')
        lens += int(len(s))
    else:
        print(s + '.')
        lens += int(len(s))
        print(lens)
