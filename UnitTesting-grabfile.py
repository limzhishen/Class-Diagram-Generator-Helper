
import logging
from pathlib import Path
import customtkinter
from fileReader.pythonRead import pythonRead
import os

abc=pythonRead(customtkinter.CTk(),"",logging)
filename="UnitTesting-GrabFile"
filename="fileReader/filePath.py"
path=os.getcwd()
filepath=os.path.join(path,filename)
abc.process_logic(filepath,thread_id=1)