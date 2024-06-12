from customtkinter import *
from tkinter import *

def print_selection():
    print(num.get())

app = CTk()
app.geometry("300x200")

num = StringVar()

CTkLabel(app, text="Select a programming language:").pack()

CTkRadioButton(app, text="Java", variable=num, value=".py").pack(anchor="w")
CTkRadioButton(app, text="Python", variable=num, value=1).pack(anchor="w")

CTkButton(app, text="Print Selection", command=print_selection).pack()

app.mainloop()
