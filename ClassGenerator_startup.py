from customtkinter import * 
from fileReader.filePath import Filepath
from component.OutputComponent import OutputComponent
from fileReader.InterfaceReadFile import ReadFile
from fileReader.pythonRead import python_Read
from fileReader.javaRead import java_Read
from threading import Thread
from component.ApplicationClass import Application
from data.FolderRefresh import migration_To_one,Temp_Save_Foldername,Processed_Data_Filename

class ClassGenerator_startup(Application):
    def __init__(self):
        super().__init__()
        self.geometry("700x600+500+600")
        self.selected=StringVar()
        self.processbox = OutputComponent(self)
        self.folder_textbox=CTkEntry(self,placeholder_text="File path ....",width=500)
        self.decoration()

    def decoration(self):
        # Head title
        CTkLabel(self, text="Class Generator Helper", font=CTkFont(family="Times New Roman", size=36)).grid(row=0, columnspan=6, sticky='nsew',pady=15)
        
        # File Path
        CTkLabel(self, text="Choose Folder", font=CTkFont(family="cursive", size=10)).grid(row=1, column=0, sticky='w')
        self.folder_textbox.grid(row=2, column=0,columnspan=3)
        CTkButton(self, text="Choose File", command=self.file_path,width=70).grid(row=2, column=5,padx=5)
        CTkButton(self, text="Choose Folder", command=self.folder_path,width=70).grid(row=2, column=6)
        
        # Processing file type (java python)
        CTkLabel(self, text="Import File Type", font=CTkFont(family="cursive", size=10)).grid(row=3, column=0, sticky='w')
        CTkRadioButton(self, text="Java", variable=self.selected,value=".java").grid(row=4, column=0,sticky="w")
        CTkRadioButton(self, text="Python", variable=self.selected,value=".py").grid(row=4, column=1,sticky="w")
        #add More just copy add column and value and text
        
        # Start button
        CTkButton(self, text="Start Process", command=self.start_process).grid(row=5, column=1,columnspan=2,sticky="w")
        # CTkButton(self,text="Export",command=self.start_export).grid(row=5,column=4)

        # Output message
        self.processbox.grid(row=6, column=0,columnspan=6,sticky="w")

        # Same row export type


    def start_export(self):
        pass

    def file_path(self):
        text=filedialog.askopenfile()
        if text:
            self.folder_textbox.delete("0", "end")
            self.folder_textbox.insert("0",text)

    def folder_path(self):
        text=filedialog.askdirectory()
        if text:
            self.folder_textbox.delete("0", "end")
            self.folder_textbox.insert("0",text)
        

    def start_process(self):
        try:
            self.processbox.cleanbox()
            self.check_status()
            self.logging.info_green("Process Start")
            file_thread=Thread(target=self.file_process_thread)
            file_thread.start()
        except Exception as e:
            print(e)

    def check_status(self):
        if self.selected.get() is None or self.selected.get()=="":
            raise Exception("Have not choose Anything")
        if self.folder_textbox.get() is None or self.folder_textbox.get()=="":
            raise Exception("have not insert file path yet")
        
    def file_process_thread(self):
        print("---Scanning File----")
        File=Filepath(self.folder_textbox.get(),self.selected.get(),self.logging)
        print("File Done Import")
        #Interface
        filereader=self.get_class(self.processbox,File.Full_path,self.logging)
        filereader.process()
        #### File Migration#####
        self.logging.info_green("Starting Migration")
        print("----Migration-----")
        migration_To_one(Temp_Save_Foldername,Processed_Data_Filename)
        print("Migration Done")
        self.logging.info_green("Succesfull Migration")
        #### File Migration#####

    def get_class(self,*argv)->ReadFile:
        if self.selected.get()==".py":
            return python_Read(*argv)
        elif self.selected.get()==".java":
            return java_Read(*argv)
            

if __name__ == '__main__':
    app=ClassGenerator_startup()
    set_appearance_mode("dark")
    app.mainloop()
