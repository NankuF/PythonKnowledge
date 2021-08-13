# decorator
import time


#
#
# def print_name(func):
#     def log_function_called(*args, **kwargs):
#         print(f'{func} called')
#         func(*args, **kwargs)
#
#     return log_function_called
#
#
# @print_name
# def my_name(name):
#     print('My name is', name)
#
#
# my_name('Valeriy')


###########

# decorator timer
def timer(func):
    def timer_wrap(*args, **kwargs) -> int:
        start = time.time()
        time.sleep(1)
        foo = func(*args, **kwargs)
        stop = time.time()
        print('Время выполнения ф-ии= ', stop - start)
        return foo

    return timer_wrap


@timer
def str_counter(string: str, char: str) -> int:
    return string.count(char)


print(str_counter('hello world', 'o'))


# print(timer.__dir__())
# print(str_counter.__dir__())

# class Hel:
#     cargo = 256000
#
#     def __init__(self,cargin):
#         self.cargin = cargin
# heli = Hel(cargin=25033)
# print(heli.__dir__())
# print(Hel.__dict__)
# print(heli.cargin)
