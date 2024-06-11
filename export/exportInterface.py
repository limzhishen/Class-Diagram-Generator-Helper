from abc import ABC,abstractmethod
from data.FolderRefresh import remove_Combined_file,check_Available,Processed_Data_Filename
from component.LoggingColorFormat import Changelogging
from component.OutputComponent import OutputComponent
import json,os


class Export(ABC):
    def __init__(self,output_textbox:OutputComponent,logging:Changelogging,max_worker:int=3,removefile:bool=True):
        self.output_textbox=output_textbox
        self.logging=logging
        self.removefile=removefile
        self.max_worker=max_worker
    
    def export(self):
        if check_Available(Processed_Data_Filename):
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
