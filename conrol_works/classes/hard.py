from tkinter import *

class Circle:
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r
    def area(self):
        return self.r*self.r*3.14
    def draw(self):
        root = Tk()
        root.title('control work')
        root.geometry('1280x720')
        canvas = Canvas(bg="white", width=1280, height=720)
        canvas.pack(anchor=CENTER, expand=1)
        self.x=640
        self.y=360
        left_corner=[self.x-self.r,self.y-self.r]
        right_corner=[self.x+self.r,self.y+self.r]
        canvas.create_oval(left_corner[0],left_corner[1],right_corner[0],right_corner[1])
        root.mainloop()
class Rect:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y
a=Circle(10,20,50)
b=Circle(80, 90, 10)
c=Rect(10,20)
for shapes in(a,b,c):
    print(shapes.area())
a.draw()
b.draw()
