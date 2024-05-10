from data.datatype import Temp_Save_Foldername
import os,time

def flush_Save_Folder():
    current_directory=os.getcwd()
    folder_name=Temp_Save_Foldername
    folder_path=os.path.join(current_directory,folder_name)
    #Check if exist Delete file(Confirm no error) else create one
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        time.sleep(0.5)
