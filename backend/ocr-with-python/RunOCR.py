import os
import easyocr
import LIST2JSON
import DrawTextBox


def PlayOCR(image):
    # Easy OCR
    reader = easyocr.Reader(['ko'],
                            model_storage_directory='./model',
                            user_network_directory='./model',
                            recog_network='custom')
    result = reader.readtext(image)
    for i in result:
        print(i[1])

    # 텍스트박스 그리기
    DrawTextBox.Draw(image, result)

    # List로 저장되어 있는 결과를 json으로 변환
    json_path = os.path.dirname(image) + "/" + os.path.basename(image) + ".json"
    LIST2JSON.tojson(result, json_path)


# 모듈로 호출 시 아래는 실행되지 않는다.
if __name__ == '__main__':
    PlayOCR("./TEST/demo.png")
