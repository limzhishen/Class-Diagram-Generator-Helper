from customtkinter import *
def button_event():
    print("button pressed")
app=CTk()
app.geometry("500x400")
button = CTkButton(app, text="CTkButton",command=button_event)   
button.place(relx=0.5,rely=0.5,anchor="center")
app.mainloop()