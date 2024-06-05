import re

class_pattern=r'\s*(public|private|protected)\s*(static|final|synchronized|abstract)?\s*(static|final|synchronized|abstract)?\s*([\w<>[\]]+)\s+(\w+)\s*(=\s*[^;]+)?\s*;'


line=("return false;")
abc=re.search(class_pattern,line,re.M|re.I)


if abc:
    print("hello")
    print(abc.group())
    print(abc.group(1))
    print(abc.group(2))
    print(abc.group(3))
    print(abc.group(4))
    print(abc.group(5))

    # print(abc.group(2))
else:
    print("cannot")