from customtkinter import * 
from data.filePath import Filepath
from Component.TextRedirector import OutputRedirector
from data.pythonRead import pythonRead
from threading import Thread
from Component.ApplicationClass import Application





class GenrateStarup(Application):
    def __init__(self):
        super().__init__()
        self.geometry("700x600")
        self.titletex=CTkLabel(self,text="Class Generator Helper",font=("Arial",20))
        self.textbox = CTkTextbox(self, height=200, width=650)
        # self.setState()
        self.startButon=CTkButton(self,text="Start Process",command=self.start_process) 
         #make output in GuI
        sys.stdout = OutputRedirector(self.textbox, sys.stdout)
        self.decoration()
    def decoration(self):
        self.textbox.pack()
        self.startButon.pack()

if __name__ == '__main__':
    app=GenrateStarup()
    set_appearance_mode("dark")
    app.mainloop()
