from threading import Thread,Lock
from customtkinter.windows import CTk
from data.InterfaceReadFile import ReadFile
from abc import abstractmethod
from queue import Queue
import time,logging


class ThreadFileReader(ReadFile):
    def __init__(self, gui: CTk, Full_path: dict, logging: logging, progress_line: int = 5):
        super().__init__(gui, Full_path, logging, progress_line)
        self.output_lock=Lock()
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
        print("Total Queue in {}".format(self.totalfile))
        title_line=self.gui.getline(self.gui.textbox)
        self.gui.cursor_end_newline(self.gui.textbox)
        time.sleep(0.5)
        self.start_thread(thread,path,title_line)

    def start_thread(self,thread,path,title_line):
        for i in range(thread):
            file_Scan_Thread=Thread(target=self.process_file,args=(path, i+1,title_line))
            file_Scan_Thread.start()
        #waiting for all thread end task
        path.join()
        self.gui.cleanLine(self.progess_line,self.gui.textbox)
        print("All Task Have been done")
    
    def process_file(self,path,threadid,title_line):
        while not path.empty():
            detail=path.get()
            if(len(detail)>25):
                detail_messange=detail[23:]+"..."
            else:
                detail_messange=detail+" "*(25-len(detail))
            with self.output_lock:
                scan_messange="Thread {}: Scanning '{}'".format(threadid,detail_messange)
                self.scan_details.append(scan_messange)
                self.num +=1
                self.update_progress(title_line)
            self.process_logic(detail)
            path.task_done()

    def update_progress(self,title_line):
        title=f"Scanning File ({self.num}/{self.totalfile})"
        self.gui.refresh_line(title_line,title,self.gui.textbox)
        if(len(self.scan_details)>5):
            self.scan_details.pop(0)
            self.gui.refresh_detail(self.progess_line,self.scan_details[-1],self.gui.textbox)
        else:
            print(self.scan_details[-1])

        # since the output move to tkinter so use text to delete
        # for j in range(num):
        #     sys.stdout.write("\033[F")
        #     sys.stdout.write("\033[K")

    @abstractmethod
    def process_logic(self,detail):
        pass

