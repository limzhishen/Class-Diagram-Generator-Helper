from component.LoggingColorFormat import Changelogging
from pathlib import Path
import customtkinter
from fileReader.pythonRead import python_Read
from fileReader.javaRead import java_Read
from data.classManager import classManger
import os

log=Changelogging()
abc=java_Read(customtkinter.CTk(),"",log)
filename="User.java"
path=os.getcwd()

foldername="Testing-Java/Class"
filepath=os.path.join(path,foldername)
filepath=os.path.join(filepath,filename)
log.debug_red(filepath)
#Due to the posix will change \ to / , So i need to change
filepath=Path(filepath)
filepath=filepath.as_posix()
abc.process_logic(filepath,thread_id=1,class_manager=classManger())