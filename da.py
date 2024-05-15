def add_attributes(number, id,name):
    print("add att" + id+name + str(number))  # 将 number 转换为字符串以进行连接

def add_method(number, id,name):
    print("aaaa ddddd" + id +name+ str(number))  # 将 number 转换为字符串以进行连接

def add_details(func, args,callback):
    callback(func,*args) 

def make_handler():
    sequence = 0
    def handler(func,*args):
        nonlocal sequence
        sequence += 1
        func(sequence,*args)
    return handler

handle=make_handler()
add_details(add_attributes, ("aaa","dd"),handle)
add_details(add_method, ("aaa","dd"),handle)