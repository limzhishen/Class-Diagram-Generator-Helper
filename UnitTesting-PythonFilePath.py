
import logging
import customtkinter
from fileReader.pythonRead import pythonRead
import os
from fileReader.filePath import Filepath
from Component.OutputComponent import OutputComponent


filename="UnitTesting_PythonFile"
path=os.getcwd()
filepath=os.path.join(path,filename)
File=Filepath(filepath,".py",logging)
print("File Done Import")
abc=pythonRead(OutputComponent(customtkinter.CTk()),File.Full_path,logging,testing=True)
#High Speed testing
abc.process(thread=5)