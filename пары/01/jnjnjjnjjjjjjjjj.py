# a=int(input())
# b=int(input())
#
# def decorator(func):
#     def wrapper(a,b):
#         return func(a,b)*2
#     return wrapper
#
# @decorator
# def summ(a,b):
#     return a+b
# print(summ(a,b))
#
# a=int(input())
# b=int(input())
#
# def decorator(func):
#     def wrapper(a,b):
#         func(a,b)
#         print('вызываю',func,'с аргументами',a,b)
#     return wrapper
#
# @decorator
# def summ(a,b):
#     print(a+b)
# print(summ(a,b))
print('welcome')

summ=0


def price():
    print('********************')
    print(summ)
    print('********************')
while True:
    order=str(input('1-shavarma,2-tea'))
    if order=='1':
        summ=summ+1000
    elif order=='2':
        summ=summ+100
    else:
        print('nope')
    nxt=str(input('1-order more,2-pay'))
    if nxt=='2':
        price()
        