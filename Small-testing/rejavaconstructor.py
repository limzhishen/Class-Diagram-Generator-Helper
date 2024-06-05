import re

def java_constructor_pattern(class_name):
    return (r'\s*(public|protected|private)?\s*{}\s*\(([^)]*)\)\s*\{{?'.format(class_name))

line=("public Admin(int a, String b)  ")
abc=re.match(java_constructor_pattern("Admin"),line,re.M|re.I)


if abc:
    print("hello")
    print(abc.group())
    print(abc.group(1))
    print(abc.group(2))


    # print(abc.group(2))
else:
    print("cannot")