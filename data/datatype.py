from enum import Enum
import re,os

Last_FilePath_pattern= r"([^\/]+)\/"

python_class_pattern=(r'class\s+(.*?)\s*\((.*?)\)\s*:')
python_method_pattern=(r'\s+def\s+(.*?)\s*\((.*?)\)\s*:')
python_attributes_pattern=(r'\s+self.(.*?)\s*=\s*(.*)')

Temp_Save_Foldername="TempThreadFile"
Processed_Data_Filename="Combineded_Data.txt"

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