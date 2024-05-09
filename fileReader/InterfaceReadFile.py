from abc import ABC,abstractmethod
from Component.OutputComponent import OutputComponent
import logging

class ReadFile(ABC):
    def __init__(self,output_textbox:OutputComponent,Full_path:dict,logging:logging,progress_line:int=5):
        self.output_textbox=output_textbox
        self.Full_path=Full_path
        self.num=0
        self.totalfile=0
        self.scan_details=[]
        self.logging=logging
        self.progress_line=progress_line
    @abstractmethod
    def process(self,path):
        pass