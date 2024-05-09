import re

class_pattern=(r'\s+self.(.*)\s*=\s*(.*)')

line=("     self.manage  =   manaaa")
abc=re.search(class_pattern,line,re.M|re.I)


if abc:
    print("hello")
    print(abc.group())
    print(abc.group(1))
    print(abc.group(2))
else:
    print("cannot")