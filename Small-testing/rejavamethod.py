import re

java_method_pattern=(r"\s*(public|private|protected)\s*(static|final|synchronized|abstract)?\s*([\w<>[\]]+)\s+(\w+)\s*\(([^)]*)\)\s*\{?")


line=(" else if(num<100){")
abc=re.search(java_method_pattern,line,re.M|re.I)


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