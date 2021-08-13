# 5. Вывести на экран букву "W" из символов "*" (звездочка)

s = '*'
space = ' '
print(s, space * 5, s, space * 5, s, sep='')
print(space * 1, s, space * 3, s, space * 1, s, space * 3, s, sep='')
print(space * 2, s, space * 1, s, space * 3, s, space * 1, s, sep='')
print(space * 3, s, space * 5, s, sep='')

# def print_w(s: str):
#     for h in range(5):
#         if h == 0:
#             for i in range(13):
#                 if i == 0 or i == 6:
#                     print(s, end='')
#                 if i == 12:
#                     print(s)
#                 else:
#                     print('_', end='')
#
#         if h == 1:
#             for x in range(11):
#                 if x == 1 or x == 5 or x == 6:
#                     print(s, end='')
#                 if x == 10:
#                     print(s)
#                 else:
#                     print('_', end='')
#
#         if h == 2:
#             for z in range(11):
#                 if z == 2 or z == 3 or z == 8:
#                     print(s, end='')
#                 if z == 9:
#                     print(s)
#                 else:
#                     print('_', end='')
#
#         if h == 3:
#             for z in range(11):
#                 if z == 2:
#                     print(s, end='')
#                 if z == 9:
#                     print(s)
#                 else:
#                     print('_', end='')
#
#
# print_w(s)
