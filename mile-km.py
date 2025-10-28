from tkinter import *

window = Tk()
window.minsize(width=160,height=75)

#funct
def convert():
    label2["text"] = round(float(miles.get()) * 1.609,1)


#making the stuff

label1 = Label(text="Is equal to",font=("Arial",8,"bold"))
label1.grid(row=1,column=0)

label2 = Label(text="0",font=("Arial",8,"bold"))
label2.grid(row=1,column=2)

label3 = Label(text="Miles",font=("Arial",8,"bold"))
label3.grid(row=0,column=3)

label4 = Label(text="Km",font=("Arial",8,"bold"))
label4.grid(row=1,column=3)

miles = Entry(width=5)
miles.grid(row=0,column=2)

calculate = Button(text="Calculate",command=convert)
calculate.grid(row=2,column=2)



window.mainloop()