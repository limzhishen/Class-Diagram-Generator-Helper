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
                 command = lambda:refresh_line(line,"hello",Output))

def getline(textbox:CTkTextbox):
        content=textbox.get(1.0,"end")
        line=content.count("\n")
        return (line) 
Output.insert("1.0","hhhhhhelo\n")
line=getline(Output)
print(line)
    
def refresh_line(line,messange,textbox:CTkTextbox):
        print("----------")
        print(line)
        textbox.delete(float(line),float(line+1))
        if(textbox.get(1.0,"end").count("\n")<line):
                textbox.insert(float(line),text="\n")
                textbox.insert(float(line),text=messange+"\n")
        else:
                textbox.insert(float(line),text=messange+"\n")
        print(textbox.get(1.0,"end").count("\n"))
       
        cursor_end_newline(textbox)
        
def cursor_end_newline(textbox:CTkTextbox):
        content=textbox.get(1.0,"end")
        if not content.strip() or content[-2]=="\n":
            textbox.mark_set("insert","end")
        else:
            textbox.insert("end",text="\n")  
            textbox.mark_set("insert","end")

Output.pack()
Refresh.pack()
set_appearance_mode("dark")
root.mainloop()