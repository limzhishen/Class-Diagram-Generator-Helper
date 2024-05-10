import time
import sys
details=[]
file=25
for i in range(file):
    time.sleep(0.1)
    title="Scanning File (%d/%d)"%(i+1,file)
    print(title)
    detail=("now Scanning %s") %(i+1)
    details.append(detail)
    if(len(details)>5):
        details.pop(0)
    for detail in details:
        if(len(detail)>40):
            detail=detail[:37]+"..."
        else:
            detail+=" "*(40-len(detail))
        print(detail)
    if(file-i>1):
        for j in range(len(details)+1):
            sys.stdout.write("\033[F") 
    else:
        for j in range(5):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")