from customtkinter import * 
from component.LoggingColorFormat import Changelogging


#Create Main Window
class Application(CTk):
    def __init__(self):
        self.logging=Changelogging()
        super().__init__()
        self.title("Class Generator Helper")
        self.iconbitmap("Component/Icon.ico")




if __name__ == '__main__':
    app=Application()
    set_appearance_mode("dark")
    app.mainloop()
