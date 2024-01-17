from tkinter import *

window = Tk()
window.geometry("500x500")

def raiseframe(frame):
    frame.tkraise()
    
def getfcalc():
    math = fcalcEntry.get()
    print(math)
    return eval(math)

def eval():
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
#TITLE
fcalcTitle = Label(fcalc, text="Normal Calculations",font=("Arial",25), background="light blue")
fcalcTitle.place(x=105,y=20)
#BACK BUTTON
fcalcBack = Button(fcalc, text="<--Back", command=lambda:raiseframe(startframe),font=("Arial",10))
fcalcBack.place(x=10,y=10)
#MAIN ENTRY TITLE
fcalcEntryTitle = Label(fcalc, text="Enter below:",font=("Arial",10),bg="light blue")
fcalcEntryTitle.place(x=115,y=75)
#MAIN ENTRY
fcalcEntry = Entry(fcalc)
fcalcEntry.place(x=115,y=100,width=300,height=200) # not finished here. carry on from here
#ANSWER ENTRY
fcalcAnswer = Entry(fcalc)
fcalcAnswer.place(x=115,y=335,width=300,height=50)
#ANSWER ENTRY TITLE
fcalcAnswerTitle = Label(fcalc, text="Answer:",font=("Arial", 10), bg="light blue")
fcalcAnswerTitle.place(x=115,y=310)
#SUBMIT
fcalcSubmit = Button(fcalc, text="Submit", command=getfcalc,font=("Arial",10))
fcalcSubmit.place(x=115,y=400,width=75)



#mainloop
window.mainloop()