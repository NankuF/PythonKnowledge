# 12. Дана строка.
# Разделить строку на фрагменты по три подряд идущих символа.
# В каждом фрагменте средний символ заменить на случайный символ,
# не совпадающий ни с одним из символов этого фрагмента.
# Показать фрагменты, упорядоченные по алфавиту.
import random

s = 'impossible'
alphabet = 'impossibleZ'


def part_3_str(s: str):
    new_s = s
    s_lst = []
    j = 0
    k = 3
    # делим строку по 3 символа
    for i in range(len(s)):
        s_lst.append(new_s[j:k])
        j = k
        k += 3

    # меняем средний символ согласно задаче
    nn_lst = []
    for i in s_lst:
        if len(i) == 3:
            rnd_test = random.choice(alphabet)
            rnd_s = rnd_test
            if rnd_test == i[0] or rnd_test == i[2] or rnd_test == i[1]:
                while rnd_test == i[0] or rnd_test == i[2] or rnd_test == i[1]:
                    rnd_test = random.choice(alphabet)
                    rnd_s = rnd_test

            nn_s = i[0] + rnd_s + i[2]
            nn_lst.append(nn_s)
    print('before sort:', nn_lst)
    nn_lst.sort()
    print('after sort:', nn_lst)


part_3_str(s)
