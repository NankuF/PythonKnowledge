# 9. Даны две строки.
# Вывести большую по длине строку столько раз,
# на сколько символов отличаются строки.

st1 = 'abc'
st2 = 'impossible'


def big_string(s1: str, s2: str):
    s1 = len(s1)
    s2 = len(s2)

    if s1 > s2:
        res = s1 - s2
        for i in range(res):
            print(st1)
    else:
        res = s2 - s1
        for i in range(res):
            print(st2)


big_string(st1, st2)
