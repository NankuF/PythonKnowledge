# 23. Дан текст.
# Найти сумму имеющихся в нем цифр

s = 'he11o every2body!'


def sum_int_in_str(s: str) -> int:
    lst = []
    for i in s:
        if i.isdigit():
            lst.append(int(i))
    summary = sum(lst)
    return summary


print(sum_int_in_str(s))


def sum_int_in_str2(s: str) -> int:
    lst = [int(i) for i in s if i.isdigit()]
    summary = sum(lst)
    return summary


print(sum_int_in_str2(s))
