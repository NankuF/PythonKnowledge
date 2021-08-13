# 2. Дана строка. Вывести первый, последний и средний (если он есть)) символы.

s = 'I love python'
s = 'impossible'


def string_symbol(s: str):
    lens = len(s)
    average = lens // 2
    print(f'first symbol= {s[0]};', f'last symbol= {s[-1]};', f'average symbol= {s[average]};', sep='\n')


string_symbol(s)
