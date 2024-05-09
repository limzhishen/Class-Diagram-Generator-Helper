import os

def start():
    # 获取当前工作目录
    current_directory = os.getcwd()

    # 定义要创建的文件夹名称
    folder_name = "new_folder2"

    # 使用 os.path.join() 函数连接当前工作目录和文件夹名称
    folder_path = os.path.join(current_directory, folder_name)

    # 如果文件夹不存在，则创建文件夹
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
    # 如果文件夹已经存在，则删除文件夹及其包含的所有文件
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.makedirs(folder_path)

    # 在文件夹里创建文件
    file_name = "pythfffffi.txt"
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "a+") as file:
        file.write("hello")
start()