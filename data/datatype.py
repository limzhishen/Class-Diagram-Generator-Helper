from enum import Enum
import re,os

Last_FilePath_pattern= r"([^\/]+)\/"

python_class_pattern=(r'\s*class\s+(.*?)\s*(\((.*?)\))?\s*:\s*(.*)')
python_method_pattern=(r'\s*def\s+(.*?)\s*\((.*?)\)\s*.*:')
python_attributes_pattern=(r'\s*self\.(\w+)\b')

Temp_Save_Foldername="TempThreadFile"
Processed_Data_Filename="Combineded_Data.txt"
drawIo_Save_name="Class Diagram.drawio"
drawIO_backup_name=".$Class Diagram.drawio.bkp"

class class_type(Enum):
    Abstract="abstract"
    Interface="interface"
    Class="class"

class attributes_type(Enum):
    Int="int"
    Float="float"
    String="string"
    Double='double'
    Nothing=""

class method_type(Enum):
    Private="private"
    Public="public"
    Protected="protected"
    Nothing=""

class attributes_access_type(Enum):
    Private="private"
    Public="public"
    Protected="protected"
    Nothing=""

#Cannot Use due to multithreading and dict in memory sharing type
# base_dict={
#         "name":"",
#         "type":"",
#         "implement":[],
#         "extend":[],
#         "method":[],
#         "attributes":[]
#     }

# method_dict={
#         "name":"",
#         "type":"",
#         "parameter":[]
#     }

# attributes_dict= {   
#         "name":"",
#         "type":"",
#         "access_type":""
#     }