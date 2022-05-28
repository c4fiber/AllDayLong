import json


def tojson(result, file_path="./data.json"):
    data = {}
    for i in range(len(result['text'])):
        data[i] = result['text'][i]['predicted_labels']

    with open(file_path, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

