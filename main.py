import tkinter

window = tkinter.Tk()
window.title("AND U SUCKERS KNOW THIS BECAUSE AS I SAID THIS BEFORE")
window.minsize(500,300)

#Label

my_label = tkinter.Label(text = "AS I SAID THIS BEFORE",font=("Arial",8,"bold"))
# my_labellll = tkinter.Label(text = "NOPE",font=("Time New York",24,"bold"))
# my_labelll = tkinter.Label(text = "NOPE",font=("Time New York",24,"bold"))
# my_labell = tkinter.Label(text = "NO ONE'S HAVING ICE CREAM",font=("Time New York",24,"bold"))



my_label.grid(row=1,column=1)
my_label.config(padx=100)
# my_labellll.pack()
# my_labelll.pack()
# my_labell.pack()

def button_click():
    my_label["text"] = input.get()


botton = tkinter.Button(text="NOPE",command=button_click)
botton.grid(row=2,column=2)
botton2 = tkinter.Button(text="YUP")
botton2.grid(row=1,column=3)
#Entry

input = tkinter.Entry()
input.grid(row=3,column=4)








window.mainloop()