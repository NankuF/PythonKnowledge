# 13. Дана строка.
# Заменить каждый четный символ или на 'a',
# если символ не равен 'a' или 'b',
# или на 'c' в противном случае.


s = 'ampossibae'


# s = 'aaa'


def swap_symbol(s: str):
    even_lst = []
    odd_lst = []
    # разбиваем на четный и нечетный списки
    for i in range(len(s)):
        if i % 2 == 0:
            even_lst.append(s[i])
        else:
            odd_lst.append(s[i])

    # print('even:', even_lst)
    # print('odd: ', odd_lst)

    # заполняем четный список нужными буквами
    for i, l in enumerate(even_lst):
        if l == 'a' or l == 'b':
            even_lst[i] = 'c'
        if l != 'a' and l != 'b':
            even_lst[i] = 'a'
    # print('new even:', even_lst)

    # cобираем оба списка в один
    end_lst = []
    count = 0
    len_even_lst = len(even_lst)
    len_odd_lst = len(odd_lst)
    sum_len_lst = len_even_lst + len_odd_lst

    while count < sum_len_lst:
        if count % 2 == 0:
            end_lst += even_lst[0]
            even_lst.pop(0)
            count += 1
        else:
            end_lst += odd_lst[0]
            odd_lst.pop(0)
            count += 1
    # print('end_lst: ', end_lst)

    # собираем список в строку
    end_s = ''
    for i in end_lst:
        end_s += i

    return end_s


print('result:', swap_symbol(s))


#### Вариант Романа Тетерина
START = 1
def swap_simbols(s):
    new_s = ''
    for n, e in enumerate(s, START):
        if n % 2:
            if e in 'ab':
                new_s += 'C'
            else:
                new_s += 'A'
        else:
            new_s += e
    return new_s


print('aaa')
print(swap_simbols('aaa'))
print('ampossibae')
print(swap_simbols('ampossibae'))