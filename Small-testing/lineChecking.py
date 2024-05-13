import re

python_class_pattern=(r'class\s+(.*?)\s*\((.*?)\)\s*:')
python_method_pattern=(r'\s+def\s+(.*?)\s*\((.*?)\)\s*:')
python_attributes_pattern=(r'\s+self.(.*?)\s*=\s*(.*)')



def process_logic(index):
    with open(index,"r+",encoding="utf-8") as file:
        for line in file:
            match_class=re.match(python_class_pattern,line)
            if match_class:
                print("Found Class")
                continue
            match_method=re.match(python_method_pattern,line)
            if match_method:
                print("Found Method")
                continue
            match_attributes=re.match(python_attributes_pattern,line)
            if match_attributes:
                print("Found Attributes")
                continue
        print("done Scanning")

process_logic("da.py")