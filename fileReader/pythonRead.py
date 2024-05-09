from customtkinter.windows import CTk
from Component.OutputComponent import OutputComponent
from fileReader.ThreadFileReader import ThreadFileReader
from data.datatype import *
from data.classManager import classManger
import logging
import re,time


class pythonRead (ThreadFileReader):
    def __init__(self, output_textbox: OutputComponent, Full_path: dict, logging: logging, progress_line: int = 5):
        super().__init__(output_textbox, Full_path, logging, progress_line)
        self.classManager=classManger()

    def process_logic(self, index):
        time.sleep(0.5)
        with open(index,"r+") as file:
            for line in file:
                # print(line)
                match_class=re.search(class_pattern,line)
                if match_class:
                    # print("----------------------------------------------------------")
                    self.class_process(match_class)
            # self.classManager.printout()
    
    def class_process(self,match):
        class_name=match.group(1)
        instance_info=match.group(2)
        type=class_type.Class
        extend=[]
        for info in instance_info.rstrip().rsplit(","):
            if(info=="ABC"):
                type=class_type.Abstract
            else:
                extend.append(info)
        self.classManager.add_class_name(class_name)
        self.classManager.add_class_type(type)
        self.classManager.add_extended_class(extended_class=extend)
        


