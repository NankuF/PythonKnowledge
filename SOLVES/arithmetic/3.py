# 3. Вывести на экран пять строк из нулей,
# причем количество нулей в каждой строке равно номеру строки.

symbol = '0'
repeat = 5


def five_string_and_zero(s: str, repeat) -> None:
    count = 1
    while count <= repeat:
        print(f'{count}:',s * count)
        count += 1


five_string_and_zero(symbol, repeat)
