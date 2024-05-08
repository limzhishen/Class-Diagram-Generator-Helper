import time
import tkinter as tk
import threading

def update_progress(details):
    text_widget.delete("1.0", tk.END)  # 清空文本框内容
    for detail in details:
        text_widget.insert(tk.END, detail + "\n")  # 在文本框中插入文本

def scan_files():
    global details
    for i in range(file):
        time.sleep(0.1)
        if details:
            details.pop(0)
        title = "Scanning File (%d/%d)" % (i + 1, file)
        details.insert(0, title)
        detail = "Now Scanning %s" % (i + 1)
        details.append(detail)
        if len(details) > 6:
            details.pop(1)
        if(i==file-1):
            for j in range(len(details)-1):
                details.pop(1)
        # 更新文本框内容
        text_widget.after(0, update_progress, details)

        # 更新进度条
        progress = (i + 1) / file * 100
        progress_bar.config(text="Progress: %.2f%%" % progress)

file = 50
details = []

root = tk.Tk()
root.title("File Scanning Progress")

text_widget = tk.Text(root, width=40, height=10)
text_widget.pack()

progress_bar = tk.Label(root, text="Progress: 0%")
progress_bar.pack()

# 启动扫描文件的线程
thread = threading.Thread(target=scan_files)
thread.start()

root.mainloop()
