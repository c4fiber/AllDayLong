import json


def tojson(list):
    data = {}
    for i in range(len(list)):
        data[i] = list[i][1]

    file_path = "./data.json"
    #file_path = "json이 저장될 경로를 지정 "

    with open(file_path, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)
