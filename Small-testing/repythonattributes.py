import re

class_pattern=(r'\bself\.(\w+)\b')

line=("self.classManager.add_extended_class(extended_class=extend)")
abc=re.search(class_pattern,line,re.M|re.I)


if abc:
    print("hello")
    print(abc.group())
    print(abc.group(1))
    # print(abc.group(2))
else:
    print("cannot")