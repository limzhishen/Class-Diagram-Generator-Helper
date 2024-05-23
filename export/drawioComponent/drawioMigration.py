from data.datatype import Temp_Export_Folder,drawIo_Save_name,draw_head,draw_tail
from data.FolderRefresh import migration_To_one,check_Available
import os


def Iomigration():
    if check_Available(Temp_Export_Folder):
        write_head()
        migration_To_one(Temp_Export_Folder,drawIo_Save_name,False)
        write_tail()
    else:
        print("Folder is no exist")
        
def write_head():
    with open(drawIo_Save_name,"w+",encoding="utf-8")as write_file:
        write_file.write(draw_head)
def write_tail():
    with open(drawIo_Save_name,"a+",encoding="utf-8")as write_file:
        write_file.write(draw_tail)