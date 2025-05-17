from pathlib import Path
from component.LoggingColorFormat import Changelogging
import json

class Filepath():
    def __init__(self,directory,type,logging:Changelogging) :
        self.directory=directory
        self.type=type
        self.Full_path={}
        self.logging=logging
        self.traverse_directory()

    #Read the file path and return dict
    def traverse_directory(self):
        count=0
        path = Path(self.directory)

        if path.is_file() and self.type in str(path):
            count += 1
            self.logging.debug_blue("Processing file: %s" % path)
            self.Full_path[count] = path.as_posix()

        elif path.is_dir():
            for file_path in path.rglob("*"):
                if "\\.git" in str(file_path) or "/.git" in str(file_path):
                    continue
                if "__pycache__" in str(file_path):
                    continue
                if file_path.is_file() and self.type in str(file_path):
                    count += 1
                    self.logging.debug_blue("Processing file: %s" % file_path)
                    self.Full_path[count] = file_path.as_posix()

        self.logging.info_green("Total have %d file" % count)
        print("Total have %d file" % count)
    # if save to file is need take again useless make another step
    # def FileWrite(self):
    #     for count,path in self.Full_path:

   

