from fileReader.javaRead import java_Read
from component.LoggingColorFormat import Changelogging
import customtkinter
import os,time
from fileReader.filePath import Filepath
from component.OutputComponent import OutputComponent

filename="Testing-Java"
path=os.getcwd()
filepath=os.path.join(path,filename)
File=Filepath(filepath,".java",Changelogging())
print("File Done Import")
starttime=time.time()
abc=java_Read(OutputComponent(customtkinter.CTk()),File.Full_path,Changelogging(),testing=True)
abc.process(thread=5)
endtime=time.time()
print(endtime-starttime)