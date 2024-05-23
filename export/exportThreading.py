from component.LoggingColorFormat import Changelogging
from export.exportInterface import Export
from data.datatype import drawIo_Save_name,Processed_Data_Filename,draw_head,draw_tail

from concurrent.futures import ThreadPoolExecutor

class ExportThread(Export):
    def __init__(self, logging: Changelogging, removefile: bool = False,max_woker:int=3):
        super().__init__(logging, removefile)
        self.max_worker=max_woker

    def start_thread(self):
        self.write_head()
        count=0
        with ThreadPoolExecutor(max_workers=self.max_worker) as pool:
            with open(Processed_Data_Filename,"r+",encoding="utf-8")as file:
                for line in file:
                    if line.strip():
                        count +=1
                        pool.submit(self.process,line)
        self.write_tail()
        self.logging.info_green("Total Have {} line".format(count))

    def process(self,line):
        pass

    def write_head(self):
        with open(drawIo_Save_name,"a+",encoding="utf-8")as write_file:
            write_file.write(draw_head)
    def write_tail(self):
        with open(drawIo_Save_name,"a+",encoding="utf-8")as write_file:
            write_file.write(draw_tail)