from component.LoggingColorFormat import Changelogging
from component.OutputComponent import OutputComponent
from fileReader.ThreadFileReader import Thread_File_Reader
from data.classManager import classManger
from data.datatype import *
import re,time

class java_Read(Thread_File_Reader):
    def __init__(self, output_textbox: OutputComponent, Full_path: dict, logging: Changelogging, methodwithoutclass: bool = False, progress_line: int = 5, testing: bool = False):
        super().__init__(output_textbox, Full_path, logging, methodwithoutclass, progress_line, testing)

    def process_logic(self, index, thread_id, class_manager:classManger):
       self.logging.debug_blue(f"Now Processing File with {thread_id} "+index)
       content=''
       with open (index ,"r+", encoding="utf-8")as file:
            class_name=""
            class_found=False
            for line in file:
                if not content.startswith(("private","protected","public")):
                   content=""
                content+=line.strip()
                match_class=re.search(java_class_pattern,content)
                if match_class:
                    if class_manager.check_class_name():
                        self.write_file(thread_id,class_manager)
                        class_manager=classManger()
                    class_manager.add_Filename(index)
                    self.class_process(match_class,class_manager)
                    class_name=match_class.group(2)
                    class_found = True
                    content=''
                    continue
                match_constructor=re.match(java_constructor_pattern(class_name),content)
                if match_constructor:
                    self.method_constructor(match_constructor,class_manager,class_name)
                    content=''
                    continue
                match_method=re.match(java_method_pattern,content)
                if match_method:
                    self.method_process(match_method,class_manager)
                    if self.methodwithoutclass:
                        class_found = True
                    content=''
                    continue
                match_attribute=re.search(java_attribute_pattern,content)
                if match_attribute:
                    self.attribute_process(match_attribute,class_manager)
                    content=''
            if class_found:
                self.write_file(thread_id,class_manager)
            else:
                #Some data will write in empty
                self.logging.debug_yellow("Not a Meaning File: "+index)

    def write_file(self,thread_id,class_manager):
        self.logging.info_green("Thread {} Writing File with {}".format(thread_id,class_manager.filename))
        self.logging.debug_yellow(str(thread_id)+str(class_manager.printout()))
        class_manager.write_file(thread_id)

    def method_constructor(self,match:re.match,class_manager:classManger,classname):
        type=method_access_type_mapping.get(match.group(1))
        parameter=[info.strip() for info in match.group(2).split(",") if info!='']
        class_manager.add_method(classname,type,parameter)
        
    def attribute_process(self,match:re.match,class_manager:classManger):
        attribute_name=match.group(5)
        access_type=attributes_access_type_mapping.get( match.group(1),attributes_access_type.Nothing)
        type=match.group(4)
        other = match.group(2)
        other = " ".join([other, match.group(3)]) if other and match.group(3) else other or match.group(3)

        class_manager.add_attributes(attribute_name,type,access_type,other=other)
    
    def method_process(self,match:re.match,class_manager:classManger):
        method_name=match.group(4)
        # group_parameter=match.group(5)
        parameter=[info.strip() for info in match.group(5).split(",") if info!=""]
        access_type=method_access_type_mapping.get(match.group(1))
        return_type=match.group(3)
        type=method_type_mapping.get(match.group(2),method_type.Nothing)
        class_manager.add_method(method_name,access_type,parameter,return_type,type)
        
               
    def class_process(self,match:re.match,class_manager:classManger):
        class_name=match.group(2)
        type=class_type_mapping.get(match.group(1),class_type.Class)
        instance_info =match.group(3)
        extends = []
        implements = []
        if instance_info is not None:
            extends_match = re.match(extends_pattern, instance_info)
            if extends_match:
                extends = [e.strip() for e in extends_match.group(1).split(',')]
            implements_match = re.match(implements_pattern, instance_info)
            if implements_match:
                implements = [i.strip() for i in implements_match.group(1).split(',')]
        class_manager.add_class_name(class_name)
        class_manager.add_class_type(type)
        class_manager.add_extended_class(extends)
        class_manager.add_implement_class(implements)
    
        


