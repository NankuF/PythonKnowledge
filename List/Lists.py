from pprint import pprint

lst = list()
lst = []
print(lst)
print(type(lst))
lst = [1, 2, 77]
# print(lst.index(77)) # покажет индекс числа 77. Будет 3 для [1,2,77]
# lst.append(3)  # добавит 3 в конец списка
# lst.insert(2, 99) # вставит число 99 на место индекса 2 [1,2,99,77,3]
# lst.extend([1,5,7]) # расширит список, вставив в конец 1,5,7    [1,2,99,77,3,1,5,7]
# lst.pop(1)  # удалит из [1,2,77] число 2, и сделает его return. default pop(-1)
# how return pop
# return_pop = lst.pop(0)  # в return_pop помещено число 1 из списка
# lst.remove(77) # удалить число 77 из списка
# lst_copy = lst.copy() # копируем список
# lst.reverse()  # разворачиваем список [1,2,77] [77,2,1]
# x = lst.count(77)  # посчитает сколько чисел 77 в списке
# lst.clear()  # очищает список
# lst.sort() # по дефолту сортирует от меньшего к большему (по возрастанию)
# lst.sort(reverse=True)   # сортирует по убыванию


print(lst)

song = 'cold, cold heart'

# replacing 'cold' with 'hurt'
print(song.replace('cold', 'hurt'))

song = 'Let it be, let it be, let it be, let it be'

# replacing only two occurences of 'let'
print(song.replace('Let', "don't let", 2))