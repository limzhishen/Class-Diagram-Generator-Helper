from data.FolderRefresh import remove_Combined_file,remove_folder
from data.datatype import Temp_Save_Foldername
import os

remove_Combined_file()

filepath=os.getcwd()
filepath=os.path.join(filepath,Temp_Save_Foldername)
remove_folder(filepath)
