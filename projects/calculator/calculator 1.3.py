from math import factorial
a=0
b=0
leng=0
wide=0
heig=0
rad=0
def error_1():
    print('operation  is not found')
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def summ(self,a,b):
        self.decorator_calc('*****************************************')
        print(a+b)
        c=a+b
        c=str(c)
        f.write(c)
        f.write(("\n"))
        self.decorator_calc('*****************************************')
    def mult(self,a,b):
        self.decorator_calc('*****************************************')
        print(a * b)
        c = a * b
        c = str(c)
        f.write(c)
        f.write(("\n"))
        self.decorator_calc('*****************************************')
    def minus(self,a,b):
        self.decorator_calc('*****************************************')
        print(a-b)
        c = a - b
        c = str(c)
        f.write(c)
        f.write(("\n"))
        self.decorator_calc('*****************************************')
    def delen(self,a,b):
        self.decorator_calc('*****************************************')
        print(a/b)
        c = a / b
        c = str(c)
        f.write(c)
        f.write(("\n"))
        self.decorator_calc('*****************************************')
    def stepen(self,a,b):
        self.decorator_calc('*****************************************')
        print(a**b)
        c = a ** b
        c = str(c)
        f.write(c)
        f.write(("\n"))
        self.decorator_calc('*****************************************')
    def factorial(self,a):
        print(factorial(a))
        c = factorial(a)
        c = str(c)
        f.write(c)
        f.write(("\n"))
    def root(self,a):
        self.decorator_calc('*****************************************')
        c=a**0.5
        print(c)
        c=str(c)
        f.write(c)
        f.write(("\n"))
        self.decorator_calc('*****************************************')
    def decorator_calc(self,message):
        print(message)
class Calculator_S:
    def __init__(self,leng,heig,wide,rad):
        self.leng=leng
        self.heig=heig
        self.wide=wide
        self.rad=rad
    def square_S(self,leng,wide):
        self.decorator_S('*****************************************')
        print(leng*wide)
        c = leng * wide
        c = str(c)
        f.write(c)
        f.write(("\n"))
        self.decorator_S('*****************************************')
    def circle_S(self,rad):
        self.decorator_S('*****************************************')
        Rad=rad**2
        print(Rad*3.14)
        c = Rad * 3.14
        c = str(c)
        f.write(c)
        f.write(("\n"))
        self.decorator_S('*****************************************')
    def cilinder_S(self,rad,heig):
        Rad=rad**2
        self.decorator_S('*****************************************')
        print(Rad*3.14*heig)
        c = Rad * 3.14*heig
        c = str(c)
        f.write(c)
        f.write(("\n"))
        self.decorator_S('*****************************************')
    def decorator_S(self,message):
        print(message)
class Calculator_V:
    def __init__(self,leng,wide,heig,rad):
        self.leng=leng
        self.wide=wide
        self.heig=heig
        self.rad=rad
    def decorator_V(self,message):
        print(message)
    def square_V(self,leng,wide,heig):
        self.decorator_V('*****************************************')
        c=leng*wide*heig
        print(c)
        c = str(c)
        f.write(c)
        f.write(("\n"))
        self.decorator_V('*****************************************')
    def circle_V(self,rad):
        self.decorator_V('*****************************************')
        c=3/4*3.14*rad**3
        print(c)
        c=str(c)
        f.write(c)
        f.write(("\n"))
        self.decorator_V('*****************************************')
    def cilinder_V(self,rad,heig):
        self.decorator_V('*****************************************')
        c=3.14*rad**2*heig
        print(c)
        f.write(c)
        f.write(("\n"))
        self.decorator_V('*****************************************')
def read(f):
    f.close()
    f = open('results.txt', 'r')
    print(f.read())
    f.close()
def delete(f):
    f.close
    f=open('results.txt','w')
    f.close()
def summ():
    print("for float '.'")
    a = float(input('a '))
    b = float(input('b '))
    result = Calculator(a, b)
    result.summ(result.a, result.b)
def minus():
    print("for float '.'")
    a = float(input('a '))
    b = float(input('b '))
    result = Calculator(a, b)
    result.minus(result.a, result.b)
def mult():
    print("for float '.'")
    a = float(input('a '))
    b = float(input('b '))
    result = Calculator(a, b)
    result.mult(result.a, result.b)
def delen():
    print("for float '.'")
    a = float(input('a '))
    b = float(input('b '))
    result = Calculator(a, b)
    result.delen(result.a, result.b)
def stepen():
    print("for float '.'")
    a = float(input('a '))
    b = float(input('b '))
    result = Calculator(a, b)
    result.stepen(result.a, result.b)
def factorial():
    print("for float '.'")
    a = float(input('a '))
    result = Calculator(a, b)
    result.factorial(result.a)
def root():
    print("for float '.'")
    a = float(input('a '))
    result = Calculator(a, b)
    result.root(result.a)
def basic_calculator():
    action = int(input('1-plus,2-minus,3-mult,4-delen,5-stepen,6-factorial,7-root '))
    if action == 1:
        summ()
    elif action == 2:
        minus()
    elif action == 3:
        mult()
    elif action == 4:
        delen()
    elif action==5:
        stepen()
    elif action==6:
        factorial()
    elif action==7:
        root()
    else:
        error_1()
def S_square():
    leng = float(input('lenght '))
    wide = float(input('wide '))
    result = Calculator_S(leng,heig,wide,rad)
    result.square(result.leng, result.wide)
def S_circle():
    rad = float(input('radius '))
    result = Calculator_S(leng,heig,wide,rad)
    result.circle(result.rad)
def S_cilinder():
    rad = float(input('radius '))
    heig = float(input('height '))
    result = Calculator_S(leng,heig,wide,rad)
    result.cilinder(result.rad, result.heig)
def S_calculator():
    action = int(input('1-square,2-circle,3-cilinder '))
    if action == 1:
        S_square()
    elif action == 2:
        S_circle()
    elif action == 3:
        S_cilinder()
    else:
        error_1()
def V_square():
    leng=float(input('lenght '))
    wide=float(input('wide '))
    heig=float(input('height '))
    result=Calculator_V(leng,wide,heig,rad)
    result.square_V(result.leng,result.wide,result.heig)
def V_circle():
    rad=float(input('radius '))
    result=Calculator_V(leng,wide,heig,rad)
    result.circle_V(result.rad)
def V_cilinder():
    rad=float(input('radius '))
    heig=float(input('height '))
    result=Calculator_V(leng,wide,heig,rad)
    result.cilinder_V(result.rad,result.heig)
def V_calculator():
    action = int(input('1-square,2-circle,3-cilinder '))
    if action == 1:
        V_square()
    elif action == 2:
        V_circle()
    elif action == 3:
        V_cilinder()
    else:
        error_1()
while True:
    f = open('results.txt', 'a')
    type_of_action=int(input('what do you want to do(1-basic calculator,2-calculator for S,3-calculator fir V,9-delete all results,10-show all results) '))
    if type_of_action==1:
        basic_calculator()
    elif type_of_action==2:
        S_calculator()
    elif type_of_action==3:
        V_calculator()
    elif type_of_action==9:
        delete(f)
    elif type_of_action==10:
        read(f)
    else:
        error_1()
    f.close()