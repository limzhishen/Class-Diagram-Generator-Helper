from export.exportInterface import Export
from export.drawioComponent.boxdrawio import titleText,subText,middle_line
from data.datatype import drawIo_Save_name,Processed_Data_Filename
from component.LoggingColorFormat import Changelogging
from export.drawioComponent.arrowdrawio import arrow_drawio,arrow_type
#Must Have
Y_SUBCOMPONENT=26
Y_SUBLINE=8

class drawio_export(Export):
    
    def __init__(self, logging: Changelogging):
        super().__init__(logging)
        self.filename=""
        self.name=""
        self.class_type=""
        self.implement=[]
        self.extend=[]
        self.method=[]
        self.attributes=[]
        self.num=0
        self.y_axis=0
        self.Allclassname=[]
        self.duplicate=[]
        self.duplicateStatus=False
        self.extend_duplicate=False
    
    #Duplicate Class name will make draw io not working need override and save the status
    def Deduplicate(self,name):
        if name in self.Allclassname:
            self.duplicateStatus=True
            self.duplicate.append(self.name)
            #如果是子class 的话 还好分辨，父class 的话 就没办法了,由于这属于最底层了，就不考虑再被调用的情况
        self.Allclassname.append(name)


    def process(self,line):
        # print(line)
        line_dict=self.get_dict(line)
        self.get_item_in_dict(line_dict)
        #Duplicate Class name will make draw io not working need override and save the status
        self.Deduplicate(self.name)
        id=self.name
        if self.duplicateStatus:
            id=str(len(self.duplicate))+"-"+self.name
        #write tile
        self.write_file(titleText(id,self.name,self.class_type).get_back())
        self.add_details(id,self.attributes,callback=self.add_attributes)
        self.add_details(id,None,callback=self.add_middle_line)
        self.add_details(id,self.method,callback=self.add_method)
        if self.duplicateStatus:
            self.logging.debug_red("Duplicate Class: "+self.filename+"_"+self.name)
            self.write_file(subText(id=(id+"_"+str(self.get_new_num())),parent=id,y_axis=self.get_y_axis_subtext(),name="Duplicate class name: "+self.filename).get_back())
        if self.extend_duplicate:
            self.logging.debug_red("extend Class: "+self.filename+"_"+self.name)
            self.write_file(subText(id=id+"_"+str(self.get_new_num()),parent=id,y_axis=self.get_y_axis_subtext(),name="Extended Duplicate class name: "+self.filename).get_back())
        #Because the extends only direct to the class, so every of the same class will directed to the first one
        self.add_arrow(id)
        self.duplicateStatus=False

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

    def get_new_num(self):
        self.num +=1
        return self.num

    def add_arrow(self,id):
        #lazy to change
        id=id+"_"+str(self.get_new_num())
        if self.extend ==[] and self.implement==[]:
            return
        if self.extend !=[]:
            for class_extend in self.extend:
                self.logging.debug_blue(f"Extend Line: Source {id} Target{class_extend}")
                self.write_file(arrow_drawio(id,arrow_type.extend,self.name,class_extend).get_back())
        if self.implement!=[]:
            for class_implement in self.implement:
                self.logging.debug_blue(f"Implement Line: Source{id} Target{class_implement}")
                self.write_file(arrow_drawio(id,arrow_type.implement,self.name,class_implement).get_back())
    #Check is it have extend the duplicate class name
    def check_extend(self):
        if self.extend ==[]:
            return
        self.extend_duplicate = any(extend in self.duplicate for extend in self.extend)

    #No suitable memory use more
    # #write with callback function (Clossure)
    # def add_details(self,func,*args,callback):
    #     callback(func,*args)
    # #To handle a num for sharing use
    # def num_handler(self):
    #     num=0
    #     def handle(func,args):
    #         nonlocal num
    #         func(*args,num)
    #     return handle

        
        
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

    
    def write_file(self,details):
        with open(drawIo_Save_name,"a+",encoding="utf-8")as write_file:
            write_file.write(details)
        
        

        