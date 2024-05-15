from customtkinter import * 
from fileReader.filePath import Filepath
from component.OutputComponent import OutputComponent
from fileReader.pythonRead import pythonRead
from threading import Thread
from component.ApplicationClass import Application
from data.FolderRefresh import migration_To_one

class ClassGenerator_startup(Application):
    def __init__(self):
        super().__init__()
        self.geometry("700x600+500+600")
        self.titletex=CTkLabel(self,text="Class Generator Helper",font=("Arial",20))
        self.textbox = OutputComponent(self)
        self.startButon=CTkButton(self,text="Start Process",command=self.start_process) 
        self.decoration()

    def decoration(self):
        self.textbox.pack()
        self.startButon.pack()

    def start_process(self):
        self.logging.info_green("Process Start")
        file_thread=Thread(target=self.file_process_thread)
        file_thread.start()
    
    def file_process_thread(self):
        print("---Scanning File----")
        File=Filepath(r"C:\Users\zhish\Desktop\iPrice\class-Diagram-Helper\UnitTesting_PythonFile",".py",self.logging)
        print("File Done Import")
        filereader=pythonRead(self.textbox,File.Full_path,self.logging)
        filereader.process()
        #### File Migration#####
        self.logging.info_green("Starting Migration")
        print("----Migration-----")
        migration_To_one()
        print("Migration Done")
        self.logging.info_green("Succesfull Migration")
        #### File Migration#####


if __name__ == '__main__':
    app=ClassGenerator_startup()
    set_appearance_mode("dark")
    app.mainloop()
