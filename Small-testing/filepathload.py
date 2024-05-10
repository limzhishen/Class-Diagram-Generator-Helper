from pathlib import Path

def traverse_directory(directory):
    for file_path in Path(directory).rglob("*"):
        if "\.git" in str(file_path):
            continue
        if file_path.is_file():
            print("Processing file:", file_path)


traverse_directory("c:/Users/zhish/Desktop/iPrice/class-Diagram-Helper")