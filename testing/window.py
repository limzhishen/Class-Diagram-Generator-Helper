import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import Button

def start_task():
    for i in range(101):
        progress_bar["value"] = i
        root.update_idletasks()  # 更新界面
        progress_label.config(text=f"Progress: {i}%")
        # 模拟耗时操作
        import time
        time.sleep(0.1)

# 创建主窗口
root = tk.Tk()
root.title("Progress Window")
root.geometry("400x300")

# 创建进度条和标签
progress_bar = Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress_bar.pack(pady=10)
progress_label = tk.Label(root, text="Progress: 0%")
progress_label.pack()

# 创建按钮并绑定任务开始函数
start_button = Button(root, text="Start Task", command=start_task)
start_button.pack(pady=10)

# 启动事件循环
root.mainloop()