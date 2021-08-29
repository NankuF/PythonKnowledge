# Написать программу, которая запрашивает у пользователя ввод числа.
# На введенное число она отвечает сообщением, целое оно или дробное.
# Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
# Если они совпадают, программа должна возвращать значение True, иначе False.

def even_or_odd():
    number = input('Введите число: ')
    if number.isdecimal():
        print('Число целое')
    else:
        print('Число дробное')
        parse = number.split('.')
        left = parse[0]
        right = parse[1]
        if left == right:
            return True
        else:
            return False


print(even_or_odd())
