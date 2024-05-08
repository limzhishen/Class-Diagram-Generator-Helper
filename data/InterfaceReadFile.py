from abc import ABC,abstractmethod
import customtkinter
import logging

class ReadFile(ABC):
    def __init__(self,gui:customtkinter.CTk,Full_path:dict,logging:logging,progress_line:int=5):
        self.gui=gui
        self.Full_path=Full_path
        self.num=0
        self.totalfile=0
        self.scan_details=[]
        self.logging=logging
        self.progess_line=progress_line
    @abstractmethod
    def process(self,path):
        pass