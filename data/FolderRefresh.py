from data.datatype import Temp_Save_Foldername, Processed_Data_Filename,drawIo_Save_name,drawIO_backup_name
import os,time

def refreshExport():
    current_directory = os.getcwd()
    file_path=os.path.join(current_directory,Processed_Data_Filename)
    if os.path.exists(file_path):
        return True
    else:
        return False
    
def flush_Save_Folder(folder):
    current_directory = os.getcwd()
    folder_name = folder
    folder_path = os.path.join(current_directory, folder_name)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        remove_contents(folder_path)
        time.sleep(0.5)

def migration_To_one(folder,file,check=True):
    current_directory = os.getcwd()
    folder_name = folder
    folder_path = os.path.join(current_directory, folder_name)
    
    filename = file
    filepath = os.path.join(current_directory, filename)
    if not os.path.exists(folder_path):
        print("Folder is not exist")
        return
    if check:
        if os.path.exists(filepath):
            os.remove(filepath)
    merge_folders(folder_path, filepath)
    remove_folder(folder_path)

def merge_folders(source_folder, target_file):
    with open(target_file, 'a+',encoding="utf-8") as outfile:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'r',encoding="utf-8") as infile:
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

def check_Available(file):
    filepath = os.path.join(os.getcwd(), file)
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
        
def removeioFile():
    filepath = os.path.join(os.getcwd(), drawIo_Save_name)
    backfile= os.path.join(os.getcwd(), drawIO_backup_name)
    if os.path.exists(filepath):
        os.remove(filepath)
    if os.path.exists(backfile):
        os.remove(backfile)

    

