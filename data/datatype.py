from enum import Enum

class_pattern=(r'\bclass\b\s+(\w+)(?:\(([^)]+)\))?:')
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


