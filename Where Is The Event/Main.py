from tkinter import *
root=Tk()
root.geometry('250x300')
root.title("Event Handler")

def handle_keypress(event):
    print(event.char)
root.bind("<Key>", handle_keypress)

btn=Button(text="Click Me!",bg='green',fg='black')
btn.pack()
def handle_click(event):
    print("The Button Has Been Clicked")

btn.bind("<Button-1>", handle_click)
root.mainloop()