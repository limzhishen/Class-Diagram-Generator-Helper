def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)
  
def add(x ,y):
    return x + y
  
def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print("[{}] Got:{}".format(sequence, result))
    return handler
  
handler = make_handler()
apply_async(add, (2,3), callback=handler)
print ()