import re
import os
from pathlib import Path
text = os.getcwd()
filname="abc.py"
text=os.path.join(text,filname)
jack=Path(text)
text=str(jack)
print(text)
pattern =  r"([^\\]+)\\"

match = re.search(pattern, text[::-1])

if match:
    found_text = match.group(1)[::-1]
    print("匹配到的结果:", found_text)
else:
    print("未找到匹配结果")
