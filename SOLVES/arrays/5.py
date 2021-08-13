# 5. Сформировать возрастающий массив из четных чисел.
from array import array

x = 2
y = 15


def positive_array(start: int, stop: int) -> array:
    arr = array('i')
    for i in range(start, stop):
        if i % 2 == 0:
            arr.append(i)
    return arr


print(positive_array(x, y))
