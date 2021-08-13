# 24. Дан текст.
# Найти слова, состоящие из цифр,
# и сумму чисел, которые образуют эти слова.

s = 'hello, i have 6 and 39 years old man'


def sum_int_words(s: str) -> []:
    s = s.split()
    lst_word_int = []
    for i in s:
        if i.isdigit():
            lst_word_int.append(i)

    lst_word_sum = []
    integer = 0
    for i, v in enumerate(lst_word_int):
        if len(v) == 1:
            lst_word_sum.append(int(v))
        else:
            for x in v:
                print('2:', integer)
                print('_____:', x)
                integer += int(x)
            lst_word_sum.append(integer)
    # print(lst_sum)
    return lst_word_sum, lst_word_int


print(sum_int_words(s))
