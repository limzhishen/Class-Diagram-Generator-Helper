from pathlib import Path

#Read the file path and return array
def traverse_directory(directory,type):
    Full_path=[]
    for file_path in Path(directory).rglob("*"):
        if "\.git" in str(file_path) or "/.git" in str(file_path):
            continue
        if file_path.is_file() and type in str(file_path):
            print("Processing file:", file_path)
            Full_path.append(file_path)
    return Full_path


