# 4.Вывести на экран прямоугольник, заполненный буквами А.
# Количество строк в прямоугольнике равно 5,
# количество столбцов равно 8.

s = 'A'
right = 8
bottom = 5


def rectangle(symbol: str, width: int, height: int) -> None:
    count = 1
    while count <= height:
        print(symbol * width)
        count += 1


rectangle(s, right, bottom)
