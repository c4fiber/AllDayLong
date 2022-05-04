import json


def tojson(result, file_path="./data.json"):
    data = {}
    for i in range(len(result)):
        data[i] = result[i][1]

    with open(file_path, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)
