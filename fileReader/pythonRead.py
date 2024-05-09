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

    def process_logic(self, index,thread_id):
        time.sleep(0.5)
        with open(index,"r+") as file:
            for line in file:
                match_class=re.match(python_class_pattern,line)
                if match_class:
                    self.class_process(match_class)
                    continue
                match_method=re.match(python_method_pattern,line)
                if match_method:
                    self.method_process(match_method)
                    continue
                match_attributes=re.match(python_attributes_pattern,line)
                if match_attributes:
                    self.attributes_process(match_attributes)
                    continue
            self.classManager.printout()
            self.classManager.write_file(thread_id)
    
    def class_process(self,match):
        class_name=match.group(1)
        instance_info=match.group(2)
        type=class_type.Class
        extend=[]
        for info in instance_info.rstrip().split(","):
            if(info=="ABC"):
                type=class_type.Abstract
            else:
                extend.append(info) if info!='' else None
        self.classManager.add_class_name(class_name)
        self.classManager.add_class_type(type)
        self.classManager.add_extended_class(extended_class=extend)

    def method_process(self,match):
        method_name=match.group(1)
        group_parameter=match.group(2)
        parameter=[]
        for info in group_parameter.rstrip().split(","):
            None if info == '' or info == "self" else parameter.append(info)
        self.classManager.add_method(name=method_name,parameter=parameter)
    
    def attributes_process(self,match):
        name=match.group(1)
        self.classManager.add_attributes(name=name) if(name.find("[")==-1)else None

