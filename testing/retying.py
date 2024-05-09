import re

class_pattern=('class?\s+')

line=("class ():")
abc=re.search(class_pattern,line)

print(abc)
if abc:
    print("hello")
else:
    print("cannot")