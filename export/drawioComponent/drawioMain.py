#Must Have
from export.drawioComponent.drawioarrow import arrow_drawio,arrow_type
from export.drawioComponent.drawiobox import titleText,subText,middle_line
from data.datatype import Temp_Export_Folder
from component.LoggingColorFormat import Changelogging
import threading,os
Y_SUBCOMPONENT=26
Y_SUBLINE=8

class DrawIoMain:
    def __init__(self,line_dict,logging:Changelogging,thread_id,callback_getnum=None):
        self.y_axis=0
        self.filename=""
        self.name=""
        self.class_type=""
        self.implement=[]
        self.extend=[]
        self.method=[]
        self.attributes=[]
        self.get_item_in_dict(line_dict)
        #call back to get the total num all thread
        self.get_new_num=callback_getnum
        self.logging=logging
        self.thread_id=thread_id

    def get_item_in_dict(self,line_dict):
        self.filename=line_dict["filename"]
        self.name=line_dict["name"]
        self.class_type=line_dict["type"]
        self.implement=line_dict["implement"]
        self.extend=line_dict["extend"]
        self.method=line_dict["method"]
        self.attributes=line_dict["attributes"]

    def get_y_axis_subtext(self):
        self.y_axis += Y_SUBCOMPONENT
        return self.y_axis
        
    def get_y_axis_line(self):
        self.y_axis += Y_SUBLINE

    def add_one_subtext(self,name,id):
        self.write_file(subText(id=(str(id)+"_"+str(self.get_new_num())),parent=id,y_axis=self.get_y_axis_subtext(),name=name,fontcolor="red").get_back())

    def add_middle_line(self,id,num):
        self.write_file(middle_line(id=num,parent=id,y_axis=self.y_axis).get_back())
        self.get_y_axis_line()

    def add_attributes(self,id,sub_id,y_axis,item):
        attributes_subtext=subText(sub_id,item["name"],id,y_axis)
        attributes_subtext.attributes_process(**item)
        self.write_file(attributes_subtext.get_back())
    
    def add_method(self,id,sub_id,y_axis,item):
        attributes_subtext=subText(sub_id,item["name"],id,y_axis)
        attributes_subtext.method_process(**item)
        self.write_file(attributes_subtext.get_back())
    # 不是真正意义上的callback 但是 这只是保持名字一样,
    # 特地为了试看callback for use callback not so meaningful
    def add_details(self,id,data:dict,callback):
        if data is not None:
            for item in data:
                num=self.get_new_num()
                y_axis=self.get_y_axis_subtext()
                sub_id=id+"_"+str(num)
                callback(id,sub_id,y_axis,item)
        else:
            num=self.get_new_num()
            sub_id=id+"_"+str(num)
            callback(id,sub_id)
            self.get_y_axis_subtext()

    def write_file(self,details):
        filename="export_Thread_"+str(self.thread_id)+".drawio"
        filepath=os.path.join(Temp_Export_Folder,filename)
        with open(filepath,"a+",encoding="utf-8")as write_file:
            write_file.write(details)

    

    def add_arrow(self,id):
        #lazy to change
        if self.extend ==[] and self.implement==[]:
            return
        if self.extend !=[]:
            for class_extend in self.extend:
                id=id+"_"+str(self.get_new_num())
                self.logging.debug_blue(f"Extend Line: Source {id} Target {class_extend}")
                self.write_file(arrow_drawio(id,arrow_type.extend,self.name,class_extend).get_back())
        if self.implement!=[]:
            for class_implement in self.implement:
                id=id+"_"+str(self.get_new_num())
                self.logging.debug_blue(f"Implement Line: Source{id} Target{class_implement}")
                self.write_file(arrow_drawio(id,arrow_type.implement,self.name,class_implement).get_back())