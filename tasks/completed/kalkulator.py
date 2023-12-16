class Calculator:
    def __init__(self,a,b,leng,heig,wide,rad):
        self.a=a
        self.b=b
        self.leng=leng
        self.heig=heig
        self.wide=wide
        self.rad=rad
    def summ(self,a,b):
        print(a+b)
    def mult(self,a,b):
        print(a*b)
    def minus(self,a,b):
        print(a-b)
    def delen(self,a,b):
        print(a/b)
    def square(self,len,wide):
        print(len*wide)
    def circle(self,rad):
        Rad=rad**2
        print(Rad*3.14)
    def cilinder(self,rad,heig):
        Rad=rad**2
        print(Rad*3.14*heig)
while True:
    type_of_action=str(input('do you want to calculate S'))
    if type_of_action=='no':
        a = int(input('a'))
        b = int(input('b'))
        rad = 0
        leng = 0
        wide = 0
        heig = 0
        result = Calculator(a, b,rad,leng,wide,heig)
        actition=int(input('1-plus,2-minus,3-mult,4-delen'))
        if actition==1:
            result.summ(result.a,result.b)
        elif actition==2:
            result.minus(result.a,result.b)
        elif actition==3:
            result.mult(result.a,result.b)
        else:
            result.delen(result.a,result.b)
    else:
        rad=int(input('radius'))
        leng=int(input('lenght'))
        wide=int(input('wide'))
        heig=int(input('height'))
        a = 0
        b = 0
        result = Calculator(a,b,leng,heig,wide,rad)
        action=int(input('1-square,2-circle,3-cilinder'))
        if action==1:
            result.square(result.leng,result.wide)
        elif action==2:
            result.circle(result.rad)
        else:
            result.cilinder(result.rad, result.heig)