from component.OutputComponent import OutputComponent
from export.exportThreading import ExportThread
from export.drawioComponent.drawiobox import titleText,subText,middle_line
from component.LoggingColorFormat import Changelogging
from data.FolderRefresh import removeioFile,flush_Save_Folder
from data.datatype import Temp_Export_Folder
from export.drawioComponent.drawioMain import DrawIoMain

#code-var-annotated
class drawio_export(ExportThread):
    
    def __init__(self, output_textbox: OutputComponent, logging: Changelogging, max_worker: int = 3, removefile: bool = True):
        super().__init__(output_textbox, logging, max_worker, removefile)
        self.num=0
        self.Allclassname=[]
        self.duplicate=[]
        self.duplicateStatus=False
        self.extend_duplicate=False
        flush_Save_Folder(Temp_Export_Folder)
        #remove the io file
        removeioFile()

        #for using the threading
    
    #Duplicate Class name will make draw io not working need override and save the status
    def Deduplicate(self,name):
        if name in self.Allclassname:
            self.duplicateStatus=True
            self.duplicate.append(name)
            #如果是子class 的话 还好分辨，父class 的话 就没办法了,由于这属于最底层了，就不考虑再被调用的情况
        self.Allclassname.append(name)


    def process(self,line,thread_id):
        drawio=DrawIoMain(self.get_dict(line),self.logging,thread_id,callback_getnum=self.get_new_num)
        #Duplicate Class name will make draw io not working need override and save the status
        self.Deduplicate(drawio.name)
        self.check_extend(drawio)
        id=drawio.name
        if self.duplicateStatus:
            id=str(len(self.duplicate))+"-"+drawio.name
        #write tile
        drawio.write_file(titleText(id,drawio.name,drawio.class_type).get_back())
        drawio.add_details(id,drawio.attributes,callback=drawio.add_attributes)
        drawio.add_details(id,None,callback=drawio.add_middle_line)
        drawio.add_details(id,drawio.method,callback=drawio.add_method)
        if self.duplicateStatus:
            self.logging.debug_red("Duplicate Class: "+drawio.filename+"  "+drawio.name)
            drawio.add_one_subtext("Duplicate class name: "+drawio.filename+" "+drawio.name,id)
        if self.extend_duplicate:
            self.logging.debug_red("extend Class: "+drawio.filename+"  "+drawio.name)
            drawio.add_one_subtext("Extended Duplicate class name: "+drawio.filename+" "+drawio.name ,id)
        #Because the extends only direct to the class, so every of the same class will directed to the first one
        drawio.add_arrow(id)
        self.duplicateStatus=False
        self.extend_duplicate=False

    #Check is it have extend the duplicate class name
    def check_extend(self,drawio:DrawIoMain):
        if drawio.extend ==[]:
            return
        self.extend_duplicate = any(extend in self.duplicate for extend in drawio.extend)

    def get_new_num(self):
        self.num +=1
        return self.num
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
    

    

        

        