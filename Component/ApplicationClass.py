from customtkinter import * 
from fileReader.filePath import Filepath
from fileReader.pythonRead import pythonRead
from threading import Thread
import logging

logging.basicConfig(format='Date-Time : %(asctime)s : - %(message)s', level = logging.DEBUG)


#Create Main Window
class Application(CTk):
    def __init__(self):
        self.logging=logging
        super().__init__()
        self.title("Class Generator Helper")
        self.iconbitmap("Icon.ico")




if __name__ == '__main__':
    app=Application()
    set_appearance_mode("dark")
    app.mainloop()
