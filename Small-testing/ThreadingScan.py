import time
import sys
import threading

# 用于存储每个扫描任务的详情
details = {}
file = 25

count=0
# 定义一个函数，用于扫描文件
def scan_files(scan_id):
    global count
    scan_details = []
    for i in range(file):
        time.sleep(0.3)  # 模拟扫描文件的耗时操作
        title = f"Scanning File ({i+1}/{file}) for Scan {scan_id}"
        scan_details.append(title)
        detail = f"Now Scanning {i+1} for Scan {scan_id}"
        scan_details.append(detail)
        
        # 将扫描详情存储到全局变量中
        details[scan_id] = scan_details[:]
        count  =count+1
        # 更新界面
        update_progress(scan_id)
        print(count)
        
# 定义一个函数，用于更新界面
def update_progress(scan_id):
    # sys.stdout.write("\033[H")  # 光标移动到终端顶部
    # sys.stdout.write("\033[J")  # 清空屏幕
    if scan_id in details:
        for detail in details[scan_id]:
            print(detail)
            
# 创建并启动多个线程进行文件扫描
for i in range(3):
    threading.Thread(target=scan_files, args=(i+1,)).start()
    