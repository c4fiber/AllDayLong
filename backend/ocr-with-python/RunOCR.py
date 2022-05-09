import os
import sys
import easyocr
import LIST2JSON
import DrawTextBox


def PlayOCR(image):
    # OCR
    reader = easyocr.Reader(['ko'],
                            model_storage_directory='./model',
                            user_network_directory='./model',
                            recog_network='custom')
    result = reader.readtext(image)

    # 텍스트박스 그리기
    DrawTextBox.Draw(image, result)

    # 결과를 json으로 변환
    json_path = os.path.dirname(image) + "/" + os.path.basename(image) + ".json"
    LIST2JSON.tojson(result, json_path)


if __name__ == '__main__':
    image_path = sys.argv[1]  # 명령행 인자받기
    PlayOCR(image_path)
    # PlayOCR("./TEST/demo.png")
