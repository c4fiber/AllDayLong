import easyocr
import numpy as np
import random
import cv2
import os
import LIST2JSON


# input = image src
# 텍스트박스가 그려진 결과는 원본과 동일한 경로에 저장된다.
# ex) ./TEST/demo.png -> ./TEST/ocred_demo.png
def PlayOCR(input):
    # Easy OCR
    reader = easyocr.Reader(['ko'],
                            model_storage_directory='./model',
                            user_network_directory='./model',
                            recog_network='custom')
    result = reader.readtext(input)
    for i in result:
        print(i[1])

    #  output 저장을 위한 경로 설정
    split_input = os.path.split(input)  # input의 경로와 파일명을 분할  //  [0]: 경로, [1]: 파일명
    input_address = split_input[0], input_name = split_input[1]
    output_image = input_address + "/ocred_" + input_name

    #  Draw TextBox with opencv
    img = cv2.imread(input)
    np.random.seed(42)
    COLORS = np.random.randint(0, 255, size=(255, 3), dtype="uint8")

    for i in result:
        x = i[0][0][0]
        y = i[0][0][1]
        w = i[0][1][0] - i[0][0][0]
        h = i[0][2][1] - i[0][1][1]

        color_idx = random.randint(0, 255)
        color = [int(c) for c in COLORS[color_idx]]
        img = cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)

    cv2.imwrite(output_image, img)

    # List 형식으로 저장되어 있는 결과를 json으로 변환 , input
    LIST2JSON.tojson(result, input_address + "/" + input_name + ".json")


if __name__ == '__main__':
    PlayOCR("./TEST/demo.png")
