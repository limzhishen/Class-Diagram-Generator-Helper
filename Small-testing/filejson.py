import json

# 要保存的数据
data = {
    'name': 'Filepath',
    'type': 'class',
    'implement': [],
    'extend': [],
    'method': [
        {'name': '__init__', 'type': '', 'parameter': ['directory', 'type', 'logging']},
        {'name': 'traverse_directory', 'type': '', 'parameter': []}
    ],
    'attributes': [
        {'name': 'directory', 'type': '', 'access_type': ''},
        {'name': 'type', 'type': '', 'access_type': ''},
        {'name': 'Full_path', 'type': '', 'access_type': ''},
        {'name': 'logging', 'type': '', 'access_type': ''}
    ]
}

# 保存数据到 JSON 文件
file_name = "data.json"
with open(file_name, "w") as file:
    json.dump(data, file, indent=4)
with open(file_name, "a+") as file:
    json.dump(data, file, indent=4)
with open(file_name, "a+") as file:
    json.dump(data, file, indent=4)
