from component.OutputComponent import OutputComponent
from component.LoggingColorFormat import Changelogging
from fileReader.ThreadFileReader import Thread_File_Reader
from data.datatype import *
from data.classManager import classManger
import re,time


class python_Read (Thread_File_Reader):
    def __init__(self, output_textbox: OutputComponent, Full_path: dict, logging: Changelogging, methodwithoutclass: bool = False, progress_line: int = 5, testing: bool = False):
        super().__init__(output_textbox, Full_path, logging, methodwithoutclass, progress_line, testing)
    # Solve the multiline Parameter Read Problem
    def process_logic(self, index,thread_id,class_manager:classManger):
        class_found=False
        self.logging.debug_blue(f"Now Processing File with {thread_id} "+index)
        content=''
        with open(index,"r+",encoding="utf-8") as file:
            for line in file:
                if not content.startswith(("def", "class")):
                    content=''
                content+=line.strip()
                
                match_class=re.match(python_class_pattern,content)
                if match_class:
                    #Some class may contain more than one class
                    if class_manager.check_class_name():
                        self.write_file(thread_id,class_manager)
                        class_manager=classManger()
                    class_manager.add_Filename(index)
                    self.class_process(match_class,class_manager)
                    class_found = True
                    content=''
                    continue
                match_method=re.match(python_method_pattern,content)
                if match_method:
                    self.method_process(match_method,class_manager)
                    if self.methodwithoutclass:
                        class_found = True
                    content=''
                    continue
                match_attributes=re.match(python_attributes_pattern,content)
                if match_attributes:
                    self.attributes_process(match_attributes,class_manager)
                    continue
            if class_found:
                self.write_file(thread_id,class_manager)
            else:
                #Some data will write in empty
                self.logging.debug_yellow("Not a Meaning File: "+index)

    def write_file(self,thread_id,class_manager):
        self.logging.info_green("Thread {} Writing File with {}".format(thread_id,class_manager.filename))
        self.logging.debug_yellow(str(thread_id)+str(class_manager.printout()))
        class_manager.write_file(thread_id)

    def class_process(self,match,class_manager:classManger):
        class_name=match.group(1)
        instance_info=match.group(2)
        type=class_type.Class
        extend=[]
        if instance_info is not None:
            extend = [info.strip("()") for info in instance_info.rstrip().split(",") if info != ""]
            type = class_type.Abstract if "ABC" in extend else type
        #remove ( or ) in the string
        class_name=re.sub(r'\([^)]*\)', '', class_name).strip() 
        class_manager.add_class_name(class_name)
        class_manager.add_class_type(type)
        class_manager.add_extended_class(extended_class=extend)

    def method_process(self,match,class_manager:classManger):
        method_name=match.group(1)
        group_parameter=match.group(2)
        parameter=[]
        for info in group_parameter.rstrip().split(","):
            None if info == '' or info == "self" else parameter.append(info)
        class_manager.add_method(name=method_name,parameter=parameter)

    def attributes_process(self,match,class_manager:classManger):
        name=match.group(1)
        class_manager.add_attributes(name=name) if(name.find("[")==-1)else None