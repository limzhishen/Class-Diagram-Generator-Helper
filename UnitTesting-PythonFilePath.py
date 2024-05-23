from component.LoggingColorFormat import Changelogging
import customtkinter
from fileReader.pythonRead import pythonRead
import os
from fileReader.filePath import Filepath
from component.OutputComponent import OutputComponent


# filename="UnitTesting_PythonFile"

# filename="fileReader"
filename=r"C:\Users\zhish\Desktop\iPrice\dalake"
path=os.getcwd()
filepath=os.path.join(path,filename)
File=Filepath(filepath,".py",Changelogging())
print("File Done Import")
abc=pythonRead(OutputComponent(customtkinter.CTk()),File.Full_path,Changelogging(),testing=True)
#High Speed testing
abc.process(thread=1)