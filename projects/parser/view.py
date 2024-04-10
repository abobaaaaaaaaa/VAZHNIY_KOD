from tkinter import *
from tkinter import ttk
from model import Parser
from control import Checker

def pars(page, container, container_class):
    global object_for_pars
    object_for_pars = Parser(page.get(), container.get(), container_class.get())
    a=object_for_pars.request_answer()
    if Checker.check_page(a) == True:
        object_for_pars = object_for_pars.parser()
        object_for_pars=Checker.check_result(object_for_pars)
        if object_for_pars!=False:
            output = ttk.Label(text=object_for_pars)
            output.pack()
        else:
            output = ttk.Label(text='wrong input data')
            output.pack()
    else:
        output=ttk.Label(text=Checker.check_page(object_for_pars.request_answer()))
        output.pack()

root = Tk()
root.geometry('1280x720')
root.title('parserЪ')
page_input = ttk.Entry()
container_input = ttk.Entry()
container_class_input = ttk.Entry()
page_input.pack()
container_input.pack()
container_class_input.pack()
comp = ttk.Button(text='complete', command=lambda: pars(page_input, container_input, container_class_input))
comp.pack()
root.mainloop()
