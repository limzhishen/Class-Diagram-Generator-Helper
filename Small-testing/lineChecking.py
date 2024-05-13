import re,time

python_class_pattern=(r'class\s+(.*?)\s*\((.*?)\)\s*:')
python_method_pattern=(r'\s*def\s+(.*?)\s*\((.*?)\)\s*:')
python_attributes_pattern=(r'\s*self.(.*?)\s*=\s*(.*)')



def process_logic(index):
    with open(index,"r+",encoding="utf-8") as file:
        content=''
        for line in file:
            if not content.rstrip().startswith(("def", "class")):
                    content=''
            content+=line.strip()
            print(content)
            match_class=re.match(python_class_pattern,content)
            if match_class:
                content=''
                print("Found Class")
                continue
            match_method=re.match(python_method_pattern,content)
            if match_method:
                content=''
                print("Found Method")
                continue
            match_attributes=re.match(python_attributes_pattern,content)
            if match_attributes:
                content=''
                print("Found Attributes")
            
            time.sleep(1.0)

        print("done Scanning")

process_logic("da.py")