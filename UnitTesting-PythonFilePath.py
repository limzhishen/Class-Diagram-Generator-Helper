from component.LoggingColorFormat import Changelogging
import customtkinter
from fileReader.pythonRead import pythonRead
import os,time
from fileReader.filePath import Filepath
from component.OutputComponent import OutputComponent


# filename="UnitTesting_PythonFile"

filename="fileReader"
path=os.getcwd()
filepath=os.path.join(path,filename)
File=Filepath(filepath,".py",Changelogging())
print("File Done Import")
starttime=time.time()
abc=pythonRead(OutputComponent(customtkinter.CTk()),File.Full_path,Changelogging(),testing=True)
#High Speed testing
abc.process(thread=5)

endtime=time.time()
print(endtime-starttime)