from data.datatype import Temp_Save_Foldername, Processed_Data_Filename
import os,time

def flush_Save_Folder():
    current_directory = os.getcwd()
    folder_name = Temp_Save_Foldername
    folder_path = os.path.join(current_directory, folder_name)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        remove_contents(folder_path)
        time.sleep(0.5)

def migration_To_one():
    current_directory = os.getcwd()
    folder_name = Temp_Save_Foldername
    folder_path = os.path.join(current_directory, folder_name)
    
    filename = Processed_Data_Filename
    filepath = os.path.join(current_directory, filename)
    
    if os.path.exists(filepath):
        os.remove(filepath)
    merge_folders(folder_path, filepath)
    remove_folder(folder_path)

def merge_folders(source_folder, target_file):
    with open(target_file, 'a') as outfile:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as infile:
                    outfile.write(infile.read())
    
def remove_folder(folder_path):
    remove_contents(folder_path)
    os.rmdir(folder_path)

def remove_contents(folder_path):
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for name in dirs:
            os.rmdir(os.path.join(root, name))

def check_Available():
    filepath = os.path.join(os.getcwd(), Processed_Data_Filename)
    if os.path.exists(filepath):
        return True
    else:
        return False
    
def remove_Combined_file():
    current_directory=os.getcwd()
    filename = Processed_Data_Filename
    filepath = os.path.join(current_directory, filename)
    if os.path.exists(filepath):
        os.remove(filepath)