import sys
import os

# 将项目根目录添加到 sys.path 中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from component.LoggingColorFormat import Changelogging
from pathlib import Path
import customtkinter
from fileReader.pythonRead import python_Read
from fileReader.javaRead import java_Read
from data.classManager import classManger


log=Changelogging()
#Type
abc=java_Read(customtkinter.CTk(),{},log)
# abc=python_Read(customtkinter.CTk(),{},log)
filename="User.java"
path=os.getcwd()

foldername="Testing-Java/Class"
filepath=os.path.join(path,foldername)
filepath=os.path.join(filepath,filename)

log.debug_red(filepath)
#Due to the posix will change \ to / , So i need to change
pathfile=Path(filepath)
filepath_posix:str=pathfile.as_posix()
abc.process_logic(filepath_posix,thread_id=1,class_manager=classManger())