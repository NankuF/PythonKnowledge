# 6.  Сформировать убывающий массив из чисел, которые делятся на 3.
from array import array

x = 15
y = 0
z = -1


def negative_array(start: int, stop: int, step: int) -> array:
    arr = array('i')
    for i in range(start, stop, step):
        if i % 3 == 0:
            arr.append(i)
    return arr


print(negative_array(x, y, z))
