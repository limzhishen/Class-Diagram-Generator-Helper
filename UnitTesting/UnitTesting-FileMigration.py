import sys
import os

# 将项目根目录添加到 sys.path 中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.FolderRefresh import migration_To_one,Temp_Save_Foldername,Processed_Data_Filename





migration_To_one(Temp_Save_Foldername,Processed_Data_Filename)