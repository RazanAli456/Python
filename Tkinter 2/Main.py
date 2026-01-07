from tkinter import *
root=Tk()
root.title('My First Window')
root.geometry('400x300')
def display():
    Name=NameEntry.get()
    message="Welcome " +Name +"\n"+"Welcome To The Coding Class"
    TextMessage.insert(END,message)
#Adding Widgets
lbl=Label(master=root,text="Hi :D",bg='green',fg='light blue',height=1,width=300)
lblname=Label(master=root,text="enter your full name",bg='yellow',fg='red')
NameEntry=Entry()
TextMessage=Text(height=4)
Btn=Button(text="Submit",height=1,bg='purple',fg='black',command=display)
lbl.pack()
lblname.pack()
NameEntry.pack()
TextMessage.pack()
Btn.pack()


root.mainloop()