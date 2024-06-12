from component.LoggingColorFormat import Changelogging
from component.OutputComponent import OutputComponent
from export.exportInterface import Export
from data.datatype import drawIo_Save_name,Processed_Data_Filename,draw_head,draw_tail
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from queue import Queue

class ExportThread(Export):
    def __init__(self, output_textbox: OutputComponent, logging: Changelogging, max_worker: int = 3, removefile: bool = True):
        super().__init__(output_textbox, logging, max_worker, removefile)
        

    def start_thread(self):
        print("Waiting For Queue to complete")
        path=self.getTask()
        total_file=path.qsize()
        self.logging.info_green(f"Total Queue for export {total_file}")
        print(f"Total Queue for export {total_file}")
        threads=[]
        for i in range(self.max_worker):
            export_thread=Thread(target=self._process,args=(path,i+1))
            export_thread.start()
            threads.append(export_thread)
        for t in threads:
            t.join()
        print("Export is done")

        
    def _process(self,path:Queue,thread_id):
        while not path.empty():
            detail=path.get()
            self.process(detail,thread_id)
            path.task_done()
    
    def process(self,line,thread_id):
        pass
    
    def getTask(self)->Queue:
        jobs=Queue()
        with open(Processed_Data_Filename,"r+",encoding="utf-8")as file:
            for line in file:
                if line.strip():
                    jobs.put(str(line))
        return jobs

