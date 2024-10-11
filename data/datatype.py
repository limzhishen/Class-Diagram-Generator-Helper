from enum import Enum
import re,os

Last_FilePath_pattern= r"([^\/]+)\/"
#python
python_class_pattern=(r'\s*class\s+(.*?)\s*(\((.*?)\))?\s*:\s*(.*)')
python_method_pattern=(r'\s*def\s+(.*?)\s*\((.*)\)\s*.*:')
python_attributes_pattern=(r'\s*self\.(\w+)\b')
#java
# java_class_pattern=(r"(public|protected|private|abstract|final)?\s*class\s+(\w+)\s*(extends\s+\w+|implements\s+[\w\s,]+)?")
java_class_pattern = r"(public|protected|private|abstract|final)?\s*(class|interface)\s+(\w+)\s*(extends\s+\w+|implements\s+[\w\s,]+)?"
extends_pattern = r'extends\s+([\w, ]+)'
implements_pattern = r'implements\s+([\w, ]+)'
java_method_pattern=(r"\s*(public|private|protected)?\s*(static|final|synchronized|abstract)?\s*([\w<>[\]]+)\s+(\w+)\s*\(([^)]*)\)\s*\{?")
java_attribute_pattern=r'\s*(public|private|protected)\s*(static|final|synchronized|abstract)?\s*(static|final|synchronized|abstract)?\s*([\w<>[\]]+)\s+(\w+)\s*(=\s*[^;]+)?\s*;'

# java_constructor_pattern = r'\s*(public|protected|private)?\s*{class_name}\s*\(([^)]*)\)\s*\{?'
def java_constructor_pattern(class_name):
    return (r'\s*(public|protected|private)?\s*{}\s*\(([^)]*)\)\s*\{{?'.format(class_name))


Temp_Save_Foldername="TempThreadFile"
Processed_Data_Filename="Combineded_Data.txt"
drawIo_Save_name="Class Diagram.drawio"
drawIO_backup_name=".$Class Diagram.drawio.bkp"
Temp_Export_Folder="TempExportThread"

draw_head="""<mxGraphModel>
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
"""
draw_tail="""
      </root>
</mxGraphModel>
"""

class class_type(Enum):
    Abstract="abstract"
    Interface="interface"
    Final="final"
    Class="class"



class method_type(Enum):
    Static="static"
    Final="final"
    Synchronized="synchronized"
    Abstract="abstract"
    Void="void"
    Nothing=""

class method_access_type(Enum):
    Private="private"
    Public="public"
    Protected="protected"
    Nothing=""

class attributes_access_type(Enum):
    Private="private"
    Public="public"
    Protected="protected"
    Nothing=""

class_type_mapping = {
    "interface": class_type.Interface,
    "abstract": class_type.Abstract,
    "final": class_type.Final
}
method_access_type_mapping={
    "private":method_access_type.Private,
    "public":method_access_type.Public,
    "protected":method_access_type.Protected
}
method_type_mapping={
    "static":method_type.Static,
    "final":method_type.Final,
    "synchronized":method_type.Synchronized,
    "abstract":method_type.Abstract,
    "void":method_type.Void
}
attributes_access_type_mapping={
    "private":attributes_access_type.Private,
    "public": attributes_access_type.Public,
    "protected":attributes_access_type.Protected
}


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