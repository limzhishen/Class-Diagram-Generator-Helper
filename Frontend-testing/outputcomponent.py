
import customtkinter as ck
 
root = ck.CTk()
root.geometry("300x300")
root.title(" Q&A ")
 
def delete_last_line(textbox:ck.CTkTextbox):
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
    

     
l = ck.CTkLabel(root,text = "What is 24 * 5 ? ")
inputtxt = ck.CTkTextbox(root, height = 100,
                width = 300,
                bg_color = "light yellow",)
 
Output = ck.CTkTextbox(root, height = 100, 
              width = 300, 
              bg_color = "light cyan")
 
Display = ck.CTkButton(root, height = 50,
                 width = 50, 
                 text ="Show",
                 command = lambda:delete_last_line(Output))
 
l.pack()
inputtxt.pack()
Display.pack()
Output.pack()
 
root.mainloop()