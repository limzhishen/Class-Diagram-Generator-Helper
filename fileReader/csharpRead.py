from component.LoggingColorFormat import Changelogging
from component.OutputComponent import OutputComponent
from fileReader.ThreadFileReader import Thread_File_Reader
from data.classManager import classManger
from data.datatype import *
import re, time


class csharp_Read(Thread_File_Reader):
    def __init__(self, output_textbox: OutputComponent, Full_path: dict, logging: Changelogging, methodwithoutclass: bool = False, progress_line: int = 5, testing: bool = False):
        super().__init__(output_textbox, Full_path, logging, methodwithoutclass, progress_line, testing)

    def process_logic(self, index, thread_id):
        self.logging.debug_blue(f"[C#] Now Processing File with Thread {thread_id}: {index}")
        try:
            with open(index, "r", encoding="utf-8") as file:
                lines = file.readlines()
        except Exception as e:
            self.logging.debug_red(f"Error reading file {index}: {e}")
            return

        class_stack = []
        current_manager = None
        brace_count = 0

        for line in lines:
            stripped = line.strip()
            if not stripped or stripped.startswith("using") or stripped.startswith("namespace"):
                continue

            # Check for class declaration
            match_class = re.search(csharp_class_pattern, stripped)
            if match_class:
                if current_manager:
                    # If nested, push current context
                    class_stack.append((current_manager, brace_count))

                current_manager = classManger()
                current_manager.add_Filename(index)
                self.class_process(match_class, current_manager)

                brace_count = 0  # Reset for new class scope
                if "{" in stripped:
                    brace_count += stripped.count("{") - stripped.count("}")
                continue

            # Count braces if within a class
            if current_manager:
                brace_count += stripped.count("{") - stripped.count("}")

                # Handle properties
                match_property = re.search(csharp_property_pattern, stripped)
                if match_property:
                    self.property_process(match_property, current_manager)
                    continue

                # Handle methods
                match_method = re.search(csharp_method_pattern, stripped)
                if match_method:
                    self.method_process(match_method, current_manager)
                    continue

                # End of current class if brace count balanced
                if brace_count <= 0:
                    self.write_file(thread_id, current_manager)
                    current_manager = None
                    if class_stack:
                        current_manager, brace_count = class_stack.pop()

        # Final write if class still open
        if current_manager:
            self.write_file(thread_id, current_manager)

    def write_file(self, thread_id, class_manager):
        self.logging.info_green(f"Thread {thread_id} Writing File with {class_manager.filename}")
        self.logging.debug_yellow(f"{thread_id} {class_manager.printout()}")
        class_manager.write_file(thread_id)

    def class_process(self, match, class_manager: classManger):
        class_name = match.group(3)
        base_classes = match.group(4).split(",") if match.group(4) else []
        base_classes = [b.strip() for b in base_classes]

        class_manager.add_class_name(class_name)
        class_manager.add_class_type(class_type.Class)
        class_manager.add_extended_class(base_classes)

    def method_process(self, match, class_manager: classManger):
        method_name = match.group(4)
        parameters = [p.strip() for p in match.group(5).split(",") if p.strip()]
        class_manager.add_method(method_name, parameter=parameters)

    def property_process(self, match, class_manager: classManger):
        access = match.group(1) or ''
        static_flag = match.group(2) or ''
        var_type = match.group(3)
        prop_name = match.group(4)
        other = static_flag.strip()
        access_enum = attributes_access_type_mapping.get(access.strip(), attributes_access_type.Nothing)
        class_manager.add_attributes(name=prop_name, type=var_type, access_type=access_enum, other=other)

