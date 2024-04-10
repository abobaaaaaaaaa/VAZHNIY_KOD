from tkinter import *
from tkinter import ttk
from model import Parser
from control import Checker

def pars(page_input, container_input, container_class_input):
    page = page_input.get()
    container = container_input.get()
    container_class = container_class_input.get()

    object_for_pars = Parser(page, container, container_class)
    a = object_for_pars.request_answer()

    if Checker().check_page(page, a):
        result = object_for_pars.parser()
        result = Checker().check_result(result)
        if result:
            output = ttk.Label(root, text=result)
            output.pack()
        else:
            output = ttk.Label(root, text='wrong input data')
            output.pack()
    else:
        output = ttk.Label(root, text='Page check failed')
        output.pack()

root = Tk()
root.geometry('1280x720')
root.title('parserЪ')

page_label = ttk.Label(root, text="Page:")
page_label.pack()
page_input = ttk.Entry(root)
page_input.pack()

container_label = ttk.Label(root, text="Container:")
container_label.pack()
container_input = ttk.Entry(root)
container_input.pack()

container_class_label = ttk.Label(root, text="Container Class:")
container_class_label.pack()
container_class_input = ttk.Entry(root)
container_class_input.pack()

comp = ttk.Button(root, text='complete', command=lambda: pars(page_input, container_input, container_class_input))
comp.pack()

root.mainloop()
