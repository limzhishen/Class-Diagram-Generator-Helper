import sys
import os

# 将项目根目录添加到 sys.path 中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from component.LoggingColorFormat import Changelogging
import customtkinter
from fileReader.pythonRead import python_Read
import time
from fileReader.filePath import Filepath
from component.OutputComponent import OutputComponent


# filename="UnitTesting_PythonFile"

filename="fileReader"
path=os.getcwd()
filepath=os.path.join(path,filename)
#Put Testing file here
filepath=r''
File=Filepath(filepath,".py",Changelogging())
print("File Done Import")
starttime=time.time()
abc=python_Read(OutputComponent(customtkinter.CTk()),File.Full_path,Changelogging(),testing=True)
#High Speed testing
abc.process(thread=5)

endtime=time.time()
print(endtime-starttime)