import sys
import os

# 将项目根目录添加到 sys.path 中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from fileReader.javaRead import java_Read
from component.LoggingColorFormat import Changelogging
import customtkinter
import time
from fileReader.filePath import Filepath
from component.OutputComponent import OutputComponent
from fileReader.pythonRead import python_Read

filename="Testing-Java\testing.java"
path=os.getcwd()
filepath=os.path.join(path,filename)
changelogging=Changelogging()
#PUt file for testing
filepath=r""
File=Filepath(filepath,".java",changelogging)
print("File Done Import")
starttime=time.time()
abc=python_Read(OutputComponent(customtkinter.CTk()),File.Full_path,changelogging,testing=True)
abc.process(thread=1)
endtime=time.time()

rangetime=endtime-starttime
changelogging.debug_red(str(rangetime))