from abc import ABC,abstractmethod
from data.FolderRefresh import remove_Combined_file,check_Available
from Component.LoggingColorFormat import Changelogging
import json,os


class Export(ABC):
    def __init__(self,logging:Changelogging,removefile:bool=False):
        self.logging=logging
        self.removefile=removefile
    
    def export(self):
        if check_Available():
            self.logging.info_green("----Start Export----")
            print("----Start Export----")
            self.start_thread()
            self.logging.info_green("----Done Export----")
            print("----Done Export----")
            if self.removefile:
                remove_Combined_file()
        else:
            self.logging.critical_red("File Not Exist")
            print("The Valid File is not in here")
    
    @abstractmethod
    def start_thread(self):
        pass

    def get_dict(self,json_str)->dict:
        return json.loads(json_str)
