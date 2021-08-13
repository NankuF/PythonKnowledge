# 7. Создать массив из n первых чисел Фибоначчи.
from array import array

n = 10

def array_fibo(n:int):
    f1 = 1
    f2 = 1
    count = 0
    while count <n-2:
        fib_sum = f1 + f2
        f1 = f2
        f2 = fib_sum
        count +=1
        print(f2)

array_fibo(n)