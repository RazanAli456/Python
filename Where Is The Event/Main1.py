from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry('250x300')
root.title("Scan For Viruses")
def Virus():
    messagebox.showwarning("Alert", "Stop! Virus Found.") 
btn=Button(text="Scan For Viruses",command=Virus)
btn.pack()
root.mainloop()