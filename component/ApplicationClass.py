import customtkinter as ck
from component.LoggingColorFormat import Changelogging
import os

#Create Main Window
class Application(ck.CTk):
    def __init__(self):
        self.logging=Changelogging()
        super().__init__()
        self.title("Class Generator Helper")
        self.iconbitmap(os.path.join(os.path.dirname(__file__), 'Icon.ico'))





if __name__ == '__main__':
    app=Application()
    ck.set_appearance_mode("dark")
    app.mainloop()
