from customtkinter import * 
from data.filePath import Filepath
from Component.TextRedirector import OutputRedirector
import logging
from data.pythonRead import pythonRead
from threading import Thread

logging.basicConfig(format='Date-Time : %(asctime)s : - %(message)s', level = logging.DEBUG)


#Create Main Window
class Application(CTk):
    def __init__(self):
        self.textboxstate=False
        self.logging=logging
        super().__init__()
        self.title("Class Generator Helper")
        self.iconbitmap("Icon.ico")
       
        


    def start_process(self):
        logging.debug("Process Start")
        print("button pressed")
        file_thread=Thread(target=self.file_process_thread).start()
    
    def file_process_thread(self):
        File=Filepath("C:\\Users\zhish\Desktop\JavaAssignmentforpresentation\src\POMSystem\Class",".java",self.logging)
        print("File Done Import")
        filereader=pythonRead(self,File.Full_path,self.logging)
    
        filereader.process()

    def setState(self):
        if(self.textboxstate):
            self.textboxstate=False
            self.textbox.configure(state="normal")
        else:
            self.textboxstate=True
            self.textbox.configure(state="disabled")


    #FOR OUTPUT Clean
    def getline(self,textbox:CTkTextbox):
        content=textbox.get(1.0,"end")
        line=content.count("\n")
        return (line) 

    def cleanLine(self,num,textbox:CTkTextbox):
        content=textbox.get(1.0,"end")
        line=content.count("\n")
        textbox.delete(float(line-num),"end")
        self.cursor_end_newline(textbox)       
    
    def refresh_line(self,line,messange,textbox:CTkTextbox):
        textbox.delete(float(line),float(line+1))
        if(textbox.get(1.0,"end").count("\n")<line):
                textbox.insert(float(line),text="\n")
                textbox.insert(float(line),text=messange+"\n")
        else:
                textbox.insert(float(line),text=messange+"\n")
        self.cursor_end_newline(textbox)
        
    def refresh_detail(self,count,messange,textbox:CTkTextbox):
        content=textbox.get("1.0","end")
        line_count=content.count("\n")
        textbox.delete(float(line_count-count),float(line_count-count+1))
        textbox.insert(float(line_count-1),messange+"\n")
        self.cursor_end_newline(textbox)

    def cursor_end_newline(self,textbox:CTkTextbox):
        content=textbox.get(1.0,"end")
        if not content.strip() or content[-2]=="\n":
            textbox.mark_set("insert","end")
        else:
            textbox.insert("end",text="\n")  
            textbox.mark_set("insert","end")

    def delete_last_line(self,textbox:CTkTextbox):
        content=textbox.get("1.0","end")
        line_count=content.count("\n")
        linecontent=textbox.get(float(line_count),"end")
        if(line_count==1):
            textbox.delete(float(line_count),"end")
        elif(line_count==2):
            textbox.delete(float(line_count),"end")
            textbox.delete(float(line_count-1),"end")
        elif(linecontent.strip()):
            textbox.delete(float(line_count),"end")
            textbox.insert(index=float(line_count),text="\n")
        else:
            textbox.delete(float(line_count),"end")
            textbox.delete(float(line_count-1),"end")
            textbox.insert(index=float(line_count),text="\n")


if __name__ == '__main__':
    app=Application()
    set_appearance_mode("dark")
    app.mainloop()
