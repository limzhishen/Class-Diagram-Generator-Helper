from customtkinter.windows import CTk
from component.OutputComponent import OutputComponent
from component.LoggingColorFormat import Changelogging
from fileReader.ThreadFileReader import ThreadFileReader
from data.datatype import *
from data.classManager import classManger
import re,time


class pythonRead (ThreadFileReader):
    def __init__(self, output_textbox: OutputComponent, Full_path: dict, logging: Changelogging, progress_line: int = 5, testing: bool = False):
        super().__init__(output_textbox, Full_path, logging, progress_line, testing)
        self.classManager=classManger()

    # def process_logic(self, index,thread_id):
    #     class_found=False
    #     self.logging.debug_blue("Now Processing File "+index)
    #     with open(index,"r+",encoding="utf-8") as file:
    #         for line in file:
    #             match_class=re.match(python_class_pattern,line)
    #             if match_class:
    #                 self.class_process(match_class)
    #                 class_found = True
    #                 continue
    #             match_method=re.match(python_method_pattern,line)
    #             if match_method:
    #                 self.method_process(match_method)
    #                 class_found = True
    #                 continue
    #             match_attributes=re.match(python_attributes_pattern,line)
    #             if match_attributes:
    #                 self.attributes_process(match_attributes)
    #                 continue
    #         if class_found:
    #             self.classManager.add_Filename(index)
    #             self.logging.info_green("Thread %s Writing File "%thread_id)
    #             self.classManager.write_file(thread_id)
    #         else:
    #             self.logging.debug_yellow("Not a Meaning File: "+index)
    # Solve the multiline Parameter Read Problem
    def process_logic(self, index,thread_id):
        class_found=False
        self.logging.debug_blue("Now Processing File "+index)
        content=''
        with open(index,"r+",encoding="utf-8") as file:
            for line in file:
                if not content.startswith(("def", "class")):
                    content=''
                    content+=line.strip()
                match_class=re.match(python_class_pattern,line)
                if match_class:
                    self.class_process(match_class)
                    class_found = True
                    content=''
                    continue
                match_method=re.match(python_method_pattern,line)
                if match_method:
                    self.method_process(match_method)
                    class_found = True
                    content=''
                    continue
                match_attributes=re.match(python_attributes_pattern,line)
                if match_attributes:
                    self.attributes_process(match_attributes)
                    continue
            if class_found:
                self.classManager.add_Filename(index)
                self.logging.info_green("Thread %s Writing File "%thread_id)
                self.classManager.write_file(thread_id)
            else:
                self.logging.debug_yellow("Not a Meaning File: "+index)


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