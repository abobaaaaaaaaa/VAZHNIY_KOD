from math import e,factorial
import timeit
n=int(input())
def stierling_factor(n):
    pi=22/7
    nn=n**n
    ee=e**n
    comma=nn/ee
    befroot=2* pi *n
    root=befroot**0.5
    factorial_stierling= root * comma
    return factorial_stierling
def math_factorial(n):
    global etalon
    etalon=factorial(n)
    return factorial(n)
def bas_cycle_factorial(n):
    factorial_for = 1

    for i in range(2, n + 1):
        factorial_for *= i

    return factorial_for
def fac(n):
    if n == 1:
        return 1
    return fac(n - 1) * n
time_recursive = timeit.timeit(lambda: fac(n), number=100000)
time_stierling=timeit.timeit(lambda:stierling_factor(n), number=100000)
time_math=timeit.timeit(lambda:math_factorial(n), number=100000)
time_for=timeit.timeit(lambda :bas_cycle_factorial(n), number=100000)
print('pogr of rec',100-fac(n)*100/etalon)
print('pogr of stierling',100-stierling_factor(n)*100/etalon)
print('pogr of for',100-bas_cycle_factorial(n)*100/etalon)
print('time of for',time_for)
print('time of math',time_math)
print('time of stierling',time_stierling)
print('time of recurs',time_recursive)