from tkinter import *
from ui import * # fix ImportError: circular import

test = "5+5"

# very unsecure code. change asap
def getfcalc():
    math = fcalcEntry.get()
    print(math)
    evaluated = eval(math)
    print(evaluated)
    fcalcAnswer.delete(0, END)
    fcalcAnswer.insert(END,evaluated)
    return evaluated


print(eval(test))