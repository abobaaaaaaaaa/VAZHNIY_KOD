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
            output = ttk.Label(root, text=result, font=("Arial", 14))
            output.pack()
            f = open('results.txt', 'a')
            f.write(str(page))
            f.write(("\n"))
            f.write(str(container))
            f.write(("\n"))
            f.write(str(container_class))
            f.write(("\n"))
            f.write(str(result))
            f.write(("\n"))
            f.write('************************************************************************************************************')
            f.write(("\n"))
            f.close()
        else:
            output = ttk.Label(root, text='wrong input data', font=("Arial", 14))
            output.pack()
    else:
        output = ttk.Label(root, text='Page check failed', font=("Arial", 14))
        output.pack()
def pars_random_jokes():
    result=Parser('https://www.anekdot.ru/random/anekdot/','text','div')
    result.random_jokes()
root = Tk()
root.geometry('1280x720')
root.title('parserЪ')
page_label = ttk.Label(root, text="Page:", font=("Arial", 14))
page_label.pack()
page_input = ttk.Entry(root, width=500)
page_input.pack()

container_label = ttk.Label(root, text="Container:", font=("Arial", 14))
container_label.pack()
container_input = ttk.Entry(root, width=500)
container_input.pack()

container_class_label = ttk.Label(root, text="Container Class:", font=("Arial", 14))
container_class_label.pack()
container_class_input = ttk.Entry(root, width=500)
container_class_input.pack()

comp = ttk.Button(root, text='complete', command=lambda: pars(page_input, container_input, container_class_input))
comp.pack()
joker=ttk.Button(root,text='10 random jokes',command=pars_random_jokes)
joker.pack(anchor=SE)
root.mainloop()
