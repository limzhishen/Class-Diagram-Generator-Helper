from component.OutputComponent import OutputComponent
from component.LoggingColorFormat import Changelogging
from fileReader.ThreadFileReader import Thread_File_Reader
from data.datatype import *
from data.classManager import classManger
import re, time, ast


class New_python_Read(Thread_File_Reader):
    def __init__(self, output_textbox: OutputComponent, Full_path: dict, logging: Changelogging, methodwithoutclass: bool = False, progress_line: int = 5, testing: bool = False):
        super().__init__(output_textbox, Full_path, logging, methodwithoutclass, progress_line, testing)

    def process_logic(self, index, thread_id):
        self.logging.debug_blue(f"[AST] Now Processing File with Thread {thread_id}: {index}")

        try:
            with open(index, "r", encoding="utf-8") as file:
                tree = ast.parse(file.read(), filename=index)
        except Exception as e:
            self.logging.debug_red(f"Failed to parse file {index}: {e}")
            return

        found_any_class = False
        standalone_methods = []

        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                class_manager = classManger()
                class_manager.add_Filename(index)

                class_name = node.name
                bases = [base.id for base in node.bases if isinstance(base, ast.Name)]
                ctype = class_type.Abstract if "ABC" in bases else class_type.Class

                class_manager.add_class_name(class_name)
                class_manager.add_class_type(ctype)
                class_manager.add_extended_class(extended_class=bases)

                for sub_node in ast.walk(node):
                    if isinstance(sub_node, ast.FunctionDef):
                        method_name = sub_node.name
                        params = [arg.arg for arg in sub_node.args.args if arg.arg != "self"]
                        class_manager.add_method(name=method_name, parameter=params)

                    elif isinstance(sub_node, (ast.Assign, ast.AnnAssign)):
                        targets = []
                        if isinstance(sub_node, ast.Assign):
                            targets = sub_node.targets
                        elif isinstance(sub_node, ast.AnnAssign):
                            targets = [sub_node.target]

                        for target in targets:
                            if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and target.value.id == "self":
                                class_manager.add_attributes(name=target.attr)


                self.write_file(thread_id, class_manager)
                found_any_class = True

            elif isinstance(node, ast.FunctionDef):
                if self.methodwithoutclass:
                    method_name = node.name
                    params = [arg.arg for arg in node.args.args]
                    standalone_methods.append((method_name, params))

        # Write standalone functions if allowed
        if standalone_methods and self.methodwithoutclass:
            class_manager = classManger()
            class_manager.add_Filename(index)
            for method_name, params in standalone_methods:
                class_manager.add_method(name=method_name, parameter=params)
            self.write_file(thread_id, class_manager)

        if not found_any_class and not standalone_methods:
            self.logging.debug_yellow(f"[AST] Not a Meaning File: {index}")

    def write_file(self, thread_id, class_manager):
        self.logging.info_green("Thread {} Writing File with {}".format(thread_id, class_manager.filename))
        self.logging.debug_yellow(str(thread_id) + str(class_manager.printout()))
        class_manager.write_file(thread_id)
