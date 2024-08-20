from customtkinter import * 
from fileReader.filePath import Filepath
from component.OutputComponent import OutputComponent
from fileReader.InterfaceReadFile import ReadFile
from fileReader.pythonRead import python_Read
from fileReader.javaRead import java_Read
from threading import Thread
from component.ApplicationClass import Application
from data.FolderRefresh import migration_To_one,Temp_Save_Foldername,Processed_Data_Filename,refreshExport
from export.drawio import drawio_export
from export.drawioComponent.drawioMigration import Iomigration

class ClassGenerator_startup(Application):
    def __init__(self):
        super().__init__()
        self.geometry("700x600+500+600")
        self.selected=StringVar()
        self.selected_export=StringVar(value="drawio")
        self.method_class=BooleanVar()
        self.processbox = OutputComponent(self)
        self.folder_textbox=CTkEntry(self,placeholder_text="File path ....",width=500)
        self.export_status=False
        self.checkExport()
        self.decoration()
        self.thread_num=3

        
    def decoration_export(self):
        #Start Export
        CTkButton(self,text="Export",state=(NORMAL if self.export_status else DISABLED),command=self.start_export).grid(row=7,column=2,columnspan=3,padx=(0, 20),pady=(10,10))
    def decoration(self):
        # Head title
        CTkLabel(self, text="Class Generator Helper", font=CTkFont(family="Times New Roman", size=36)).grid(row=0, columnspan=6, sticky='nsew',pady=15)
        
        # File Path
        CTkLabel(self, text="Choose Folder", font=CTkFont(family="cursive", size=10)).grid(row=1, column=0, sticky='w',pady=(10,10))
        self.folder_textbox.grid(row=2, column=0,columnspan=4)
        CTkButton(self, text="Choose File", command=self.file_path,width=70).grid(row=2, column=5,padx=5)
        CTkButton(self, text="Choose Folder", command=self.folder_path,width=70).grid(row=2, column=6)
        
        # Processing file type (java python)
        CTkLabel(self, text="Import File Type", font=CTkFont(family="cursive", size=10)).grid(row=3, column=0, sticky='w',pady=(10,10))
        CTkRadioButton(self, text="Java", variable=self.selected,value=".java").grid(row=4, column=0,sticky="w")
        CTkRadioButton(self, text="Python", variable=self.selected,value=".py").grid(row=4, column=1,sticky="w")
        #add More just copy add column and value and text
        
        # Start button
        CTkButton(self, text="Start Process", command=self.start_process).grid(row=5, column=1,columnspan=3,padx=(0, 20),pady=(10,10))

        #Method Class?
        CTkSwitch(self, text="Method Without Class",variable=self.method_class,onvalue=True,offvalue=False).grid(row=6,column=0,columnspan=1)

        #Threading Num
        CTkLabel(self,text="Thread num: ").grid(row=6,column=4,columnspan=2)
        CTkEntry(self,width=30,placeholder_text=3).grid(row=6,column=6)
        # CTkButton(self,text="Export",command=self.start_export).grid(row=5,column=4)
        
        #Refresh Button
        CTkButton(self,text="Refresh",command=self.checkExport).grid(row=7,column=0,columnspan=3)

        self.decoration_export()

        # Export file type (drawio)
        CTkLabel(self, text="Export File Type", font=CTkFont(family="cursive", size=10)).grid(row=8, column=0, sticky='w',pady=(10,10))
        CTkRadioButton(self, text="DrawIO", variable=self.selected_export,value="drawio").grid(row=8, column=0,sticky="w")
        #add More just copy add column and value and text

        # Output message
        self.processbox.grid(row=9, column=0,columnspan=6,sticky="w")

        # Same row export type

    def checkExport(self):
        if refreshExport():
            self.export_status=True
        else:
            self.export_status=False
        self.decoration_export()

    def start_export(self):
        #Make Process box writeable
        self.processbox.setState(True)
        try:
            self.processbox.cleanbox()
            self.logging.info_green("Export Start")
            #Create a new thread make ui can running
            file_thread=Thread(target=self.export_process_thread)
            file_thread.start()
        except Exception as e:
            print(e)
        self.processbox.setState(False)

    def export_process_thread(self):
        #thread main try catch will not catch exception thread
        try:
            print("Export Starting....")
            export_File=self.get_export_Type(self.processbox,self.logging,self.thread_num,True)
            print("Type="+self.selected_export.get())
            export_File.export()
            print("----Migration-----")
            if self.selected_export.get()=="drawio":
                Iomigration()
                print("Migration Done")
                print("\tYou Can Open the Class Diagram File")
                print ("----Tips For Arrange----")
                print("Arrange->Layout->Horizontal Flow")
                print("Arrange->Layout->Vertical Flow")
            self.checkExport()
        except Exception as e:
            print("Export is Fail!! raise issue in https://github.com/limzhishen/Class-Diagram-Generator-Helper/issues")
            print(e)
            

    #Add Export here
    def get_export_Type(self,*argv):
        if self.selected_export.get()=="drawio":
            return drawio_export(*argv)
        else:
            raise BrokenPipeError("None Class")

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
        #Make textbox writeable
        self.processbox.setState(True)
        try:
            self.processbox.cleanbox()
            self.check_status()
            self.logging.info_green("Process Start")
            #Create a new thread make ui can running
            file_thread=Thread(target=self.file_process_thread)
            file_thread.start()
        except Exception as e:
            print(e)
        self.checkExport()
        self.processbox.setState(False)

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
        print(self.method_class.get())
        filereader=self.get_class(self.processbox,File.Full_path,self.logging,self.method_class.get())
        filereader.process(self.thread_num if self.thread_num is not None else 3)
        #### File Migration#####
        self.logging.info_green("Starting Migration")
        print("----Migration-----")
        migration_To_one(Temp_Save_Foldername,Processed_Data_Filename)
        print("Migration Done")
        self.logging.info_green("Succesfull Migration")
        # File Migration

    #Add Reader here
    def get_class(self, *argv)->ReadFile:
        if self.selected.get()==".py":
            return python_Read(*argv)
        elif self.selected.get()==".java":
            return java_Read(*argv)
        else:
            raise BrokenPipeError("None Class")
            

if __name__ == '__main__':
    app=ClassGenerator_startup()
    set_appearance_mode("dark") #type: ignore
    app.mainloop()
