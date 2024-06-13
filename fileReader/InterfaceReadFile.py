from abc import ABC,abstractmethod
from component.OutputComponent import OutputComponent
from component.LoggingColorFormat import Changelogging
from data.FolderRefresh import flush_Save_Folder,Temp_Save_Foldername

class ReadFile(ABC):
    def __init__(self,output_textbox:OutputComponent,Full_path:dict|None,logging:Changelogging,methodwithoutclass:bool=False,progress_line:int=5,testing:bool=False):
        self.output_textbox=output_textbox
        self.Full_path=Full_path
        self.num=0
        self.totalfile=0
        self.scan_details=[]
        self.logging=logging
        self.methodwithoutclass=methodwithoutclass
        self.progress_line=progress_line
        #prevent GUi while Testing
        self.testing=testing
        #flush the save place 
        flush_Save_Folder(Temp_Save_Foldername)
    @abstractmethod
    def process(self,path):
        pass