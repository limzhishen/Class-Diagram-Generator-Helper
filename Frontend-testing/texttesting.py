
from customtkinter import *
 
root = CTk()
root.geometry("300x300")
root.title(" Q&A ")
Output = CTkTextbox(root, height = 100, 
              width = 300, 
              bg_color = "light cyan")
 
Refresh = CTkButton(root, height = 50,
                 width = 50, 
                 text ="Refresh",
                 command = lambda:refresh_liine(2,"hello",Output))
Detail = CTkButton(root, height = 50,
                 width = 50, 
                 text ="Detail",
                 command = lambda:refresh_detail(3,"hiiiiiiii",Output))
Check = CTkButton(root, height = 50,
                 width = 50, 
                 text ="Detail",
                 command = lambda:cursor_end_newline(Output))
 
def refresh_liine(line,messange,textbox:CTkTextbox):
        textbox.delete(float(line),float(line+1))
        textbox.insert(float(line),text=messange+"\n")
        
        
def refresh_detail(count,messange,textbox:CTkTextbox):
        content=textbox.get("1.0","end")
        line_count=content.count("\n")
        textbox.delete(float(line_count-count),float(line_count-count+1))
        textbox.insert(float(line_count-1),messange+"\n")
def cursor_end_newline(textbox:CTkTextbox):
        content=textbox.get(1.0,"end")
        if not content.strip() or content[-2]=="\n":
            textbox.mark_set("insert","end")
        else:
            textbox.insert("end",text="\n")  
            textbox.mark_set("insert","end") 


Output.pack()
Refresh.pack()
Detail.pack()
Check.pack()
root.mainloop()