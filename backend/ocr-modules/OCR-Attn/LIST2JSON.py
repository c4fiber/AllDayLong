import json


def tojsonsingle(result, file_path="./data.json"):
    data = {}
    for i in range(len(result['text'])):
        data[i] = result['text'][i]['predicted_labels']

    with open(file_path, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)


def tojsondual(result1, result2, file_path="./data.json"):
    data = {}
    for i in range(len(result1['text'])):
        if result1['text'][i]['confidence_score'] >= result2['text'][i]['confidence_score']:
            data[i] = result1['text'][i]['predicted_labels']
        else:
            data[i] = result2['text'][i]['predicted_labels']

    with open(file_path, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)


def tojsontrio(result1, result2, result3, file_path="./data.json"):
    data = {}
    for i in range(len(result1['text'])):
        if result1['text'][i]['confidence_score'] >= result2['text'][i]['confidence_score']:
            maxresult = result1
        else:
            maxresult = result2

        if maxresult['text'][i]['confidence_score'] >= result3['text'][i]['confidence_score']:
            data[i] = maxresult['text'][i]['predicted_labels']
        else:
            data[i] = result3['text'][i]['predicted_labels']

    with open(file_path, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)
