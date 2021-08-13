# 1. Заполнить массив нулями,
# кроме первого и последнего элементов,
# которые должны быть равны единице.
from array import array

first_and_last_el = 1
any_el = 0


def one_and_zero_array(x: int, y: int) -> array:
    arr = array('i')
    for i in range(10):
        if i == 0 or i == 9:
            arr.append(x)
        else:
            arr.append(y)
    return arr


print(one_and_zero_array(first_and_last_el, any_el))
