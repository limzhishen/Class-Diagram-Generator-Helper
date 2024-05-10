from data.datatype import *
import json
import os,logging,re
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
class classManger:
    def __init__(self,):
        self.base_dict={
        "filename":"",
        "name":"",
        "type":"",
        "implement":[],
        "extend":[],
        "method":[],
        "attributes":[]
    }


    def add_class_name(self,name):
        self.base_dict['name']=name

    def add_class_type(self,type:class_type):
        self.base_dict['type']=type.value

    def printout(self):
        print(self.base_dict)

    def add_extended_class(self,extended_class):
        # self.base_dict['extend'] = extended_class if extended_class != "" else None
        self.base_dict['extend'] = extended_class

    def add_implement_class(self,implement_class):
        self.base_dict['implement']=implement_class

    def add_attributes(self,name,type=attributes_type.Nothing,access_type=attributes_access_type.Nothing):
        new_attributes_dict={   
        "name":"",
        "type":"",
        "access_type":""
        }
        new_attributes_dict["name"]=name
        new_attributes_dict["type"]=type.value
        new_attributes_dict["access_type"]=access_type.value
        self.base_dict["attributes"].append(new_attributes_dict)

    def add_method(self,name,type=method_type.Nothing,parameter=[]):
        new_method_dict={
        "name":"",
        "type":"",
        "parameter":[]
        }
        new_method_dict["name"]=name
        new_method_dict["type"]=type.value
        new_method_dict["parameter"]=parameter
        self.base_dict["method"].append(new_method_dict)

    def add_Filename(self,filePath):
        pattern = Last_FilePath_pattern
        match=re.search(pattern,filePath[::-1])
        filename=match.group(1)[::-1]
        self.base_dict["filename"]=filename

    def write_file(self,thread_id):
        file_name="class_Thread_{}.txt".format(thread_id)
        file_path=os.path.join(Temp_Save_Foldername,file_name)
        with open(file_path,"a+",encoding='utf-8')as file:
            data=json.dumps(self.base_dict)
            file.write(data+"\n\n")