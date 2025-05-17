from component.LoggingColorFormat import Changelogging
from component.OutputComponent import OutputComponent
from fileReader.ThreadFileReader import Thread_File_Reader
from data.classManager import classManger
from data.datatype import *
import re, time

class java_Read(Thread_File_Reader):
    def __init__(self, output_textbox: OutputComponent, Full_path: dict, logging: Changelogging, methodwithoutclass: bool = False, progress_line: int = 5, testing: bool = False):
        super().__init__(output_textbox, Full_path, logging, methodwithoutclass, progress_line, testing)

    def process_logic(self, index, thread_id):
        self.logging.debug_blue(f"Now Processing File with {thread_id}: {index}")
        try:
            with open(index, "r", encoding="utf-8") as file:
                lines = file.readlines()
        except Exception as e:
            self.logging.debug_red(f"Error reading file {index}: {e}")
            return

        content = ''
        class_name = ''
        current_manager = None
        brace_count = 0
        class_found = False

        for line in lines:
            stripped = line.strip()
            if not stripped or stripped.startswith('//') or stripped.startswith('@'):
                continue

            content += ' ' + stripped

            match_class = re.search(java_class_pattern, content)
            if match_class:
                if current_manager:
                    self.write_file(thread_id, current_manager)

                current_manager = classManger()
                current_manager.add_Filename(index)
                self.class_process(match_class, current_manager)
                class_name = match_class.group(3)
                content = ''
                class_found = True
                continue

            match_constructor = re.search(java_constructor_pattern(class_name), content)
            if match_constructor and current_manager:
                self.method_constructor(match_constructor, current_manager, class_name)
                content = ''
                continue

            match_method = re.search(java_method_pattern, content)
            if match_method and current_manager:
                self.method_process(match_method, current_manager)
                content = ''
                continue

            match_attribute = re.search(java_attribute_pattern, content)
            if match_attribute and current_manager:
                self.attribute_process(match_attribute, current_manager)
                content = ''
                continue

            # Reset only if line ends
            if stripped.endswith(';') or stripped.endswith('}'):
                content = ''

        if current_manager:
            self.write_file(thread_id, current_manager)
        elif not class_found:
            self.logging.debug_yellow("Not a Meaning File: " + index)


    def write_file(self, thread_id, class_manager):
        self.logging.info_green(f"Thread {thread_id} Writing File: {class_manager.filename}")
        self.logging.debug_yellow(f"{thread_id} {class_manager.printout()}")
        class_manager.write_file(thread_id)

    def method_constructor(self, match, class_manager: classManger, classname):
        access_type = method_access_type_mapping.get(match.group(1), method_access_type.Nothing)
        parameters = [param.strip() for param in match.group(2).split(",") if param.strip()]
        class_manager.add_method(classname, access_type, parameters)

    def attribute_process(self, match, class_manager: classManger):
        attribute_name = match.group(5)
        access_type = attributes_access_type_mapping.get(match.group(1), attributes_access_type.Nothing)
        var_type = match.group(4)
        modifier = match.group(2) or ''
        modifier += " " + match.group(3) if match.group(3) else ""
        modifier = modifier.strip()

        class_manager.add_attributes(attribute_name, var_type, access_type, other=modifier)

    def method_process(self, match, class_manager: classManger):
        method_name = match.group(4)
        parameters = [param.strip() for param in match.group(5).split(",") if param.strip()]
        access_type = method_access_type_mapping.get(match.group(1), method_access_type.Public)
        return_type = match.group(3)
        method_modifier = method_type_mapping.get(match.group(2), method_type.Nothing)
        class_manager.add_method(method_name, access_type, parameters, return_type, method_modifier)

    def class_process(self, match, class_manager: classManger):
        class_name = match.group(3)
        type = class_type_mapping.get(match.group(1), class_type.Class)
        if match.group(2) == class_type.Interface.value:
            type = class_type.Interface

        extends = []
        implements = []
        instance_info = match.group(4)

        if instance_info:
            extends_match = re.search(extends_pattern, instance_info)
            if extends_match:
                extends = [e.strip() for e in extends_match.group(1).split(',')]
            implements_match = re.search(implements_pattern, instance_info)
            if implements_match:
                implements = [i.strip() for i in implements_match.group(1).split(',')]

        class_manager.add_class_name(class_name)
        class_manager.add_class_type(type)
        class_manager.add_extended_class(extends)
        class_manager.add_implement_class(implements)
