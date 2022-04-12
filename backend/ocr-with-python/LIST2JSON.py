import json


def tojson(list, file_path="./TEST/data.json"):
    data = {}
    for i in range(len(list)):
        data[i] = list[i][1]

    with open(file_path, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)
