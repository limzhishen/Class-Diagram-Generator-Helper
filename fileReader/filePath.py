from pathlib import Path
import json

class Filepath():
    def __init__(self,directory,type,logging) :
        self.directory=directory
        self.type=type
        self.Full_path={}
        self.logging=logging
        self.traverse_directory()

    #Read the file path and return dict
    def traverse_directory(self):
        count=1
        for file_path in Path(self.directory).rglob("*"):
            if "\.git" in str(file_path) or "/.git" in str(file_path):
                continue
            if file_path.is_file() and self.type in str(file_path):
                self.logging.debug("Processing file: %s", file_path)
                self.Full_path[count]=file_path.as_posix()
                count+=1
        print("Total have %d file"%count)
    # if save to file is need take again useless make another step
    # def FileWrite(self):
    #     for count,path in self.Full_path:

   

