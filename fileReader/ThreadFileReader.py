from threading import Thread,Lock
from component.OutputComponent import OutputComponent
from component.LoggingColorFormat import Changelogging
from fileReader.InterfaceReadFile import ReadFile
from abc import abstractmethod
from queue import Queue
from data.classManager import classManger
import time,threading


class Thread_File_Reader(ReadFile):
    def __init__(self, output_textbox: OutputComponent, Full_path: dict|None, logging: Changelogging, methodwithoutclass: bool = False, progress_line: int = 5, testing: bool = False):
        super().__init__(output_textbox, Full_path, logging, methodwithoutclass, progress_line, testing)
        self.lock=Lock()

       
    def getTask(self,Full_path):
        jobs=Queue()
        for num,detail in Full_path.items():
            jobs.put(str(detail))
        return jobs

    def process(self,thread=3):
        Full_path=self.Full_path
        print("Waiting For Queue to complete")
        path=self.getTask(Full_path)
        self.totalfile=path.qsize()
        self.logging.info_green("Total Queue in {}".format(self.totalfile))
        print("Total Queue in {}".format(self.totalfile))
        title_line=""
        if not self.testing:
            title_line=self.output_textbox.getline()
            self.output_textbox.cursor_end_newline()
        time.sleep(0.5)
        self.start_thread(thread,path,title_line)
        

    def start_thread(self,thread,path,title_line):
        threads=[]
        for i in range(thread):
            #Every thread need instance a new class manager class
            file_Scan_Thread=Thread(target=self.process_file,args=(path, i+1,title_line))
            file_Scan_Thread.start()
            threads.append(file_Scan_Thread)
        #waiting for all thread end task
        for t in threads:
            t.join()
        #this can prevent reqeust too many 
        time.sleep(0.1)
        if not self.testing:
            self.output_textbox.cleanLine(len(self.scan_details))
        print("All Task Have been done")

    def process_file(self,path,thread_id,title_line):
        while not path.empty():
            class_manager=classManger()
            detail=path.get()
            if(len(detail)>25):
                detail_messange=detail[23:]+"..."
            else:
                detail_messange=detail+" "*(25-len(detail))
            with self.lock:
                self.logging.debug_red(str(thread_id)+"_"+str(class_manager))
                if not self.testing:
                    scan_messange="Thread {}: Scanning '{}'".format(thread_id,detail_messange)
                    self.scan_details.append(scan_messange)
                    self.num +=1
                    self.update_progress(title_line)

            self.process_logic(detail,thread_id,class_manager)
            path.task_done()


    
    def update_progress(self,title_line):
        title=f"Scanning File ({self.num}/{self.totalfile})"
        self.output_textbox.refresh_line(title_line,title)
        if(len(self.scan_details)>5):
            self.scan_details.pop(0)
            self.output_textbox.refresh_detail(self.progress_line,self.scan_details[-1])
        else:
            print(self.scan_details[-1])

    @abstractmethod
    def process_logic(self,detail,thread_id,class_manager):
        pass