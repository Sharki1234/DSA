from tkinter import *
def get_value():
    name = entry.get()
    name_label = Label(screen,text = name,fg = "blue")
    name_label.grid(row = 3,column = 1)


screen = Tk(className="Lesson 1")
screen.geometry("500x500")
label = Label(screen,text="Name")
label.grid(row = 1,column = 1)

entry = Entry(screen)
entry.grid(row = 1,column = 2)

button = Button(screen,text = "Press",background="green",activebackground="red",fg="white",command = get_value)
button.grid(row = 2,column=1)
screen.mainloop()