import re

class_pattern=(r'\s+def\s+(.*?)\s*\((.*?)\)\s*:')

line=("    def __init__(self,directory,type,logging) :")
abc=re.match(class_pattern,line,re.M|re.I)


if abc:
    print("hello")
    print(abc.group())
    print(abc.group(1))
    print(abc.group(2))
    for info in abc.group(2).rstrip().split(","):
        print("a"+ info+"a")
        if(info!="self"):
            print("-"*50)
else:
    print("cannot")