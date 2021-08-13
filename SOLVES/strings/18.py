# 18. Удалите в строке все 'abc', за которыми следует цифра.

# РЕШЕНИЕ ХАРДКОД. НЕУНИВЕРСАЛЬНОЕ!

s = 'abc1abc2 a1abc'


def del_letters(s: str):
    new_s = ''
    ss = ''
    for i, v in enumerate(s):
        # находим 'abc' от текущего i
        first_index_in_abc = s.find('abc', i - 3, i)
        # удаляем abc и оставляем цифры
        if v.isdigit() and first_index_in_abc >= 0:
            # print('v_letter: ', v, 'z_index: ', first_index_in_abc)
            new_s += s[first_index_in_abc + 3]
            # print( first_index_in_abc ,s[first_index_in_abc+4:])
        # Хардкодим. Добавляем оставшуюся строку.
        if i > first_index_in_abc and first_index_in_abc >0:
            ss = s[first_index_in_abc+4:]
            new_s = new_s + ss

    print('ss: ', ss)
    print(new_s)


print(del_letters(s))
