# 4. Сформировать массив
# из элементов арифметической прогрессии
# с заданным первым элементом x и разностью d.
from array import array

x = 1
d = 3
end = 5


def progression(start: int, step: int, stop: int) -> array:
    prog = start
    arr = array('i')
    for i in range(stop):
        arr.append(prog)
        prog += step
    return arr


print(progression(x, d, end))
