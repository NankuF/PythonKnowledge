# 2. Заполнить массив нулями и единицами, при этом данные значения чередуются, начиная с нуля.
from array import array

x = 0
y = 1


def array_0_1(x: int, y: int) -> array:
    arr = array('i')
    for i in range(10):
        if i % 2 == 0:
            arr.append(x)
        else:
            arr.append(y)
    return arr


print(array_0_1(x, y))
