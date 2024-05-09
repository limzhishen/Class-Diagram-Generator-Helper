from customtkinter import * 
from fileReader.filePath import Filepath
from Component.OutputComponent import OutputComponent
from fileReader.pythonRead import pythonRead
from threading import Thread
from Component.ApplicationClass import Application





class GenrateStarup(Application):
    def __init__(self):
        super().__init__()
        self.geometry("700x600")
        self.titletex=CTkLabel(self,text="Class Generator Helper",font=("Arial",20))
        self.textbox = OutputComponent(self)
        self.startButon=CTkButton(self,text="Start Process",command=self.start_process) 
        self.decoration()

    def decoration(self):
        self.textbox.pack()
        self.startButon.pack()

    def start_process(self):
        self.logging.debug("Process Start")
        print("button pressed")
        file_thread=Thread(target=self.file_process_thread)
        file_thread.start()
    
    def file_process_thread(self):
        File=Filepath("C:\\Users\zhish\Desktop\JavaAssignmentforpresentation\src\POMSystem\Class",".java",self.logging)
        print("File Done Import")
        filereader=pythonRead(self.textbox,File.Full_path,self.logging)
        filereader.process()

if __name__ == '__main__':
    app=GenrateStarup()
    set_appearance_mode("dark")
    app.mainloop()
