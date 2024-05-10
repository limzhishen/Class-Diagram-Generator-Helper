from typing import Tuple
from customtkinter import *
from customtkinter.windows.widgets.font import CTkFont
from component.TextRedirector import OutputRedirector

class OutputComponent(CTkTextbox):
    def __init__(self, master: any, width: int = 650, height: int = 200, corner_radius: int | None = None, border_width: int | None = None, border_spacing: int = 3, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, text_color: str | None = None, scrollbar_button_color: str | Tuple[str, str] | None = None, scrollbar_button_hover_color: str | Tuple[str, str] | None = None, font: tuple | CTkFont | None = None, activate_scrollbars: bool = True, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, border_spacing, bg_color, fg_color, border_color, text_color, scrollbar_button_color, scrollbar_button_hover_color, font, activate_scrollbars, **kwargs)
        #make output in Textbox
        sys.stdout = OutputRedirector(self, sys.stdout)
        self.textboxstate=False

         #FOR OUTPUT Clean
    def getline(self):
        content=self.get(1.0,"end")
        line=content.count("\n")
        return (line) 

    def cleanLine(self,num):
        content=self.get(1.0,"end")
        line=content.count("\n")
        self.delete(float(line-num),"end")
        self.cursor_end_newline()       
    
    def refresh_line(self,line,messange):
        self.delete(float(line),float(line+1))
        if(self.get(1.0,"end").count("\n")<line):
                self.insert(float(line),text="\n")
                self.insert(float(line),text=messange+"\n")
        else:
                self.insert(float(line),text=messange+"\n")
        self.cursor_end_newline()
        
    def refresh_detail(self,count,messange):
        content=self.get("1.0","end")
        line_count=content.count("\n")
        self.delete(float(line_count-count),float(line_count-count+1))
        self.insert(float(line_count-1),messange+"\n")
        self.cursor_end_newline()

    def cursor_end_newline(self):
        content=self.get(1.0,"end")
        if not content.strip() or content[-2]=="\n":
            self.mark_set("insert","end")
        else:
            self.insert("end",text="\n")  
            self.mark_set("insert","end")

    def delete_last_line(self):
        content=self.get("1.0","end")
        line_count=content.count("\n")
        linecontent=self.get(float(line_count),"end")
        if(line_count==1):
            self.delete(float(line_count),"end")
        elif(line_count==2):
            self.delete(float(line_count),"end")
            self.delete(float(line_count-1),"end")
        elif(linecontent.strip()):
            self.delete(float(line_count),"end")
            self.insert(index=float(line_count),text="\n")
        else:
            self.delete(float(line_count),"end")
            self.delete(float(line_count-1),"end")
            self.insert(index=float(line_count),text="\n")

    def setState(self):
        if(self.textboxstate):
            self.textboxstate=False
            self.textbox.configure(state="normal")
        else:
            self.textboxstate=True
            self.textbox.configure(state="disabled")