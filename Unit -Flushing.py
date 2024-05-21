from data.FolderRefresh import remove_Combined_file,remove_folder,removeioFile
from data.datatype import Temp_Save_Foldername
import os

remove_Combined_file()

filepath=os.getcwd()
filepath=os.path.join(filepath,Temp_Save_Foldername)
if os.path.exists(filepath):
    remove_folder(filepath)
removeioFile()