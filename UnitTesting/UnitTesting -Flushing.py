import sys
import os

# 将项目根目录添加到 sys.path 中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from data.FolderRefresh import remove_Combined_file,remove_folder,removeioFile
from data.datatype import Temp_Save_Foldername,Temp_Export_Folder


## Remove All file

remove_Combined_file()

directory=os.getcwd()
filepath=os.path.join(directory,Temp_Save_Foldername)
if os.path.exists(filepath):
    remove_folder(filepath)
filepath=os.path.join(directory,Temp_Export_Folder)
if os.path.exists(filepath):
    remove_folder(filepath)
removeioFile()