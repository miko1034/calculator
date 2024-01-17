from tkinter import *

window = Tk()
window.geometry("500x500")

def raiseframe(frame):
    frame.tkraise()
    
def getfcalc():
    pass

#creation of all frames

fcalc = Frame(window, background="light blue")
fcalc.place(x=0,y=0,height=500,width=500)
startframe = Frame(window, background="light blue")
startframe.place(x=0,y=0,height=500,width=500)

#startframe objects
starttext = Label(startframe, text="Calculator",font=("Arial",30), background="light blue")
starttext.place(x=165,y=20)
continuebutton = Button(startframe, text="Basic Calc", command=lambda:raiseframe(fcalc),font=("Arial",15))
continuebutton.place(width=100,x=60,y=110)

#fcalc objects
fcalcTitle = Label(fcalc, text="Normal Calculations",font=("Arial",25), background="light blue")
fcalcTitle.place(x=105,y=20)
fcalcBack = Button(fcalc, text="<--Back", command=lambda:raiseframe(startframe),font=("Arial",10))
fcalcBack.place(x=10,y=10)
fcalcSubmit = Button(fcalc, text="Submit", command=getfcalc())
##actual calculator
fcalcEntry = Entry(fcalc, text="Enter Math Here")
fcalcEntry.place(x=115,y=100,width=300,height=200) # not finished here. carry on from here



window.mainloop()