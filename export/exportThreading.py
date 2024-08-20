from component.LoggingColorFormat import Changelogging
from component.OutputComponent import OutputComponent
from export.exportInterface import Export
from data.datatype import Processed_Data_Filename
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from queue import Queue
from threading import Lock

class ExportThread(Export):
    def __init__(self, output_textbox: OutputComponent, logging: Changelogging, max_worker: int = 3, removefile: bool = True,testing:bool =False):
        super().__init__(output_textbox, logging, max_worker, removefile,testing)
        self.lock=Lock()
        self.output_array=[]
        

    def start_thread(self):
        print("Waiting For Queue to complete")
        path=self.getTask()
        total_file=path.qsize()
        self.logging.info_green(f"Total Queue for export {total_file}")
        print(f"Total Queue for export {total_file}")
        threads=[]
        exceptions=[]
        for i in range(self.max_worker):
            export_thread=Thread(target=self._process,args=(path,i+1,exceptions))
            export_thread.start()
            threads.append(export_thread)
        for t in threads:
            t.join()
        if not exceptions:
            if not self.testing:
                self.output_textbox.cleanLine(len(self.output_array))
            print("Thread export is done")
        else:
            raise Exception (exceptions[0])

        
    def _process(self,path:Queue,thread_id,exception:list):
        try:
            while not path.empty():
                detail=path.get()
                self.process(detail,thread_id)
                path.task_done()
        except Exception as e:
            exception.append(e)
            return
    
    def process(self,line,thread_id):
        pass
    
    def getTask(self)->Queue:
        jobs=Queue()
        with open(Processed_Data_Filename,"r+",encoding="utf-8")as file:
            for line in file:
                if line.strip():
                    jobs.put(str(line))
        return jobs

    def update_progress(self,message):
        with self.lock:
            self.output_array.append(message)
            if(len(self.output_array)>5):
                self.output_array.pop(0)
                self.output_textbox.refresh_detail(5,self.output_array[-1])
            else:
                print(self.output_array[-1])
