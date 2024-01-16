from tkinter import *

window = Tk()
window.geometry("500x500")

startframe = Frame(window)
#startframe objects
starttext = Label(window, text="Calculator")
starttext.place(y=100)
starttext.configure(anchor="center")


mainframe = Frame(window)
#packing frames
startframe.pack()
startframe.pack_propagate(False)
startframe.configure(background="light blue", width=500,height=500)

window.mainloop()