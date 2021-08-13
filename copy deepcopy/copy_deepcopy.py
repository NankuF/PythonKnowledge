# видна разница между copy и ссылкой.
# так же данный пример показывает, что вложенный список изменяется даже с copy,
# но с deepcopy такого не произойдет
import copy

lst = ['1', 2, 3, [77, 88, 99]]
x = lst.copy()
print('x= ', x)
x.append(7)
x[3][1] = 55
print('x= ', x)
print('lst= ', lst)

print('**' * 8)

lst2 = ['cookie', 'test', [77, 88, 998]]
x2 = lst2
print('x2= ', x2)
x2.append([7, 32, (12, 7)])
x2[2][1] = 55
print('x2= ', x2)
print('lst2= ', lst2)

print('**' * 8)

lst3 = ['1', 2, 3, [77, 88, 99]]
x3 = copy.deepcopy(lst3)
print('x3= ', x3)
x3.append(7)
x3[3][1] = 55
print('x3= ', x3)
print('lst3= ', lst3)

