# 14. В данной строке найти количество цифр.

s = '1mposs1b1e'


def int_count_in_str(s: str):
    int_count = 0
    for i in range(len(s)):
        if s[i].isnumeric():
            int_count += 1
    return int_count


print(int_count_in_str(s))
