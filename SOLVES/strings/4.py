# 4. Сформировать строку из 10 символов.
# На четных позициях должны находится четные цифры,
# на нечетных позициях - буквы.

import random


def gen_str(len_string: int) -> str:
    letters = ['a', 'b', 'c', 'd', 'e']
    result = []
    for i in range(len_string):
        gen_int = str(random.randrange(2, 24, 2))
        if i % 2 == 0:
            result.append(gen_int)
        else:
            result.append(random.choice(letters))
    result = ''.join(result)
    return result


print(gen_str(10))
