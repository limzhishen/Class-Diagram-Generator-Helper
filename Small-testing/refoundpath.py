import re

text = "C:/Users/zhish/Desktop/iPrice/class-Diagram-Helper/testing/MoneyPrinterTurbo/app/config/__init__.py"
pattern = r"([^\/]+)\/"

match = re.search(pattern, text[::-1])

if match:
    found_text = match.group(1)[::-1]
    print("匹配到的结果:", found_text)
else:
    print("未找到匹配结果")
