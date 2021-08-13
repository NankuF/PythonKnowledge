# Возьмем строку "I love Python". Напишите код, который выведет символы до буквы "t".
s = 'I love Python'
lst = []
n = 0
while s[n] != 't':
    print(s[n], end='')
    lst.append(s[n])
    n += 1

print('\n')
print(''.join(lst))


# Возьмем строку "I love Python". Напишите код, который выведет эту строку без пробелов.
s = 'I love Python'
print(s.replace(' ', ''))
# или так:
# for i in s:
#     if i == ' ':
#         continue
#     else:
#         print(i, end='')

# Возьмем строку "I love Python". Напишите код, который выведет эту строку пять раз подряд.
s = 'HI love Python'
for i in range(5):
    print(s)


