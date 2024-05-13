import re

class_pattern=(r'class\s+(.*?)\s*\((.*?)\)\s*:\s*(.*)')

line=("class jo(ABC,fsds):")
abc=re.match(class_pattern,line,re.M|re.I)


if abc:
    print("hello")
    print(abc.group())
    print(abc.group(1))
    print(abc.group(2))
else:
    print("cannot")