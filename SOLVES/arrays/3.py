# 3. Заполнить массив последовательными нечетными числами, начиная с единицы.
from array import array

start_even = 1


def array_odd(start_even: int) -> array:
    arr = array('i')
    for i in range(start_even, 10):
        if i % 2 != 0:
            arr.append(i)

    return arr


print(array_odd(start_even))
