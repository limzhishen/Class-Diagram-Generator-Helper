from pathlib import Path
import json
import logging
logging.basicConfig(format='Date-Time : %(asctime)s : - %(message)s', level = logging.DEBUG)
class Filepath():
    def __init__(self,directory,type,logging) :
        self.directory=directory
        self.type=type
        self.Full_path={}
        self.logging=logging
        self.traverse_directory()

    #Read the file path and return dict
    def traverse_directory(self):
        print("hello")
        count=0
        for file_path in Path(self.directory).rglob("*"):
            print("Processing file: %s", file_path)
            if "\\.git" in str(file_path) or "/.git" in str(file_path):
                continue
            if file_path.is_file() and self.type in str(file_path):
                count+=1
                self.logging.debug("Processing file: %s", file_path)
                self.Full_path[count]=file_path.as_posix()
                
        print("Total have %d file"%count)

File=Filepath(r"C:\Users\zhish\Desktop\iPrice\class-Diagram-Helper\testing\MoneyPrinterTurbo",".py",logging)
print("File Done Import")
