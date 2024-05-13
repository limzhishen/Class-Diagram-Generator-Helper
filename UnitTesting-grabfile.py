from component.LoggingColorFormat import Changelogging
from pathlib import Path
import customtkinter
from fileReader.pythonRead import pythonRead
import os

log=Changelogging()
abc=pythonRead(customtkinter.CTk(),"",log)
filename="filePath.py"
path=os.getcwd()

foldername="fileReader"
filepath=os.path.join(path,foldername)
filepath=os.path.join(filepath,filename)
log.debug_red(filepath)
#Due to the Dict will change \ to / , So i need to change
filepath=Path(filepath)
filepath=filepath.as_posix()
abc.process_logic(filepath,thread_id=1)