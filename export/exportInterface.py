from abc import ABC,abstractmethod
from data.FolderRefresh import remove_Combined_file
from component.LoggingColorFormat import Changelogging
from data.datatype import Processed_Data_Filename,drawIo_Save_name
import json,os
head="""<mxGraphModel>
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
"""
tail="""
      </root>
</mxGraphModel>
"""

class Export(ABC):
    def __init__(self,logging:Changelogging):
        self.logging=logging
    
    def export(self):
        if self.checkexist_File():
            self.logging.info_green("----Start Export----")
            print("----Start Export----")
            self.write_head()

            with open(Processed_Data_Filename,"r+",encoding="utf-8")as file:
                for line in file:
                    if line.strip():
                        self.process(line)
            self.write_tail()
            self.logging.info_green("----Done Export----")
            print("----Done Export----")
            self.remove_File()
        else:
            self.logging.critical_red("File Not Exist")
            print("The Valid File is not in here")
    
    def write_head(self):
    #flush the content
        with open(drawIo_Save_name,"w+",encoding="utf-8")as write_file:
            write_file.write(head)
    def write_tail(self):
    #flush the content
        with open(drawIo_Save_name,"a+",encoding="utf-8")as write_file:
            write_file.write(tail)

    def checkexist_File()->bool:
        if os.path.exists(Processed_Data_Filename):
            return True
        else:
            return False
    
    @abstractmethod
    def process(self,data):
        pass

    def remove_File(self):
        remove_Combined_file()

    def get_dict(self,json_str)->dict:
        return json.loads(json_str)