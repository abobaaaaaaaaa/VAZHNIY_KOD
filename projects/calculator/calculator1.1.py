def error_1():
    print('operation  is not found')
class Calculator:
    def __init__(self,a,b,results):
        self.a=a
        self.b=b
        self.results=results
    def summ(self,a,b):
        self.decorator_calc('*****************************************')
        print(a+b)
        self.decorator_calc('*****************************************')
    def mult(self,a,b):
        self.decorator_calc('*****************************************')
        print(a*b)
        self.decorator_calc('*****************************************')
    def minus(self,a,b):
        self.decorator_calc('*****************************************')
        print(a-b)
        self.decorator_calc('*****************************************')
    def delen(self,a,b):
        self.decorator_calc('*****************************************')
        print(a/b)
        self.decorator_calc('*****************************************')
    def stepen(self,a,b):
        self.decorator_calc('*****************************************')
        print(a**b)
        self.decorator_calc('*****************************************')
    def decorator_calc(self,message):
        print(message)
class Calculator_s:
    def __init__(self,leng,heig,wide,rad):
        self.leng=leng
        self.heig=heig
        self.wide=wide
        self.rad=rad
    def square(self,len,wide):
        self.decorator_s('*****************************************')
        print(len*wide)
        self.decorator_s('*****************************************')
    def circle(self,rad):
        self.decorator_s('*****************************************')
        Rad=rad**2
        print(Rad*3.14)
        self.decorator_s('*****************************************')
    def cilinder(self,rad,heig):
        Rad=rad**2
        self.decorator_s('*****************************************')
        print(Rad*3.14*heig)
        self.decorator_s('*****************************************')
    def decorator_s(self,message):
        print(message)
results=[]
def basic_calculator():
    print("for float '.'")
    a = float(input('a'))
    b = float(input('b'))
    result = Calculator(a, b, results)
    action = int(input('1-plus,2-minus,3-mult,4-delen,5-stepen'))
    if action == 1:
        result.summ(result.a, result.b)
    elif action == 2:
        result.minus(result.a, result.b)
    elif action == 3:
        result.mult(result.a, result.b)
    elif action == 4:
        result.delen(result.a, result.b)
    elif action==5:
        result.stepen(result.a,result.b)
    else:
        error_1()
def S_square():
    leng = float(input('lenght'))
    wide = float(input('wide'))
    result = Calculator(leng, 0, wide, 0)
    result.square(result.leng, result.wide)
    results.append(result.square(result.leng, result.wide))
def S_circle():
    rad = float(input('radius'))
    result = Calculator(0, 0, 0, rad)
    result.circle(result.rad)
    results.append(result.circle(result.rad))
def S_cilinder():
    rad = float(input('radius'))
    heig = float(input('height'))
    result = Calculator(0, heig, 0, rad)
    result.cilinder(result.rad, result.heig)
    results.append(result.rad, result.heig)
def S_calculator():
    action = int(input('1-square,2-circle,3-cilinder'))
    if action == 1:
        S_square()
    elif action == 2:
        S_circle()
    elif action == 3:
        S_cilinder()
    else:
        error_1()
while True:
    type_of_action=int(input('what do you want to do(1-basic calculator,2-calculator for s,10-show all results)'))
    if type_of_action==1:
        basic_calculator()
    elif type_of_action==2:
        S_calculator()
    elif type_of_action==10:
        print(results)