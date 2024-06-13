import json

with open("Combineded_Data.txt", "r+",encoding="utf-8")as file:
    abc=file.readline()

bdc=json.loads(abc)
# print(type(abc))
# bac=(abc['method'])
# for items in bac:
#     for key,value in items.items():
#         print(value)
for key,value in bdc.items():
    print (key, value)

