from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("200x200")
root.title("Lenght Converter App!")
lbl=Label(master=root,text="Enter Lenght In Inches")
lbl.pack()
lblinput=Entry()
lblinput.pack()

def convertlenght():
    leng=float(lblinput.get())*2.54
    messagebox.showwarning("Alert", leng)


button=Button(root,text="convert", command=convertlenght)
button.place(x=40 , y=80)

root.mainloop()