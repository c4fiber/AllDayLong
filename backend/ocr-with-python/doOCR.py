import easyocr
import numpy as np
import random
import cv2
import os
import LIST2JSON


# input = image src
# 텍스트박스가 그려진 이미지는 원본과 동일한 경로에 저장된다.
# ex) test/img/demo.png -> test/img/ocred_demo.png

def PlayOCR(input):
    # Easy OCR
    reader = easyocr.Reader(['ko'],
                            model_storage_directory='./model',
                            user_network_directory='./model',
                            recog_network='custom')
    result = reader.readtext(input)

    #  Draw TextBox with opencv
    img = cv2.imread(input)
    splitedinput = os.path.split(input)  # input 이미지의 경로를 기준으로 분할
    outputimage = splitedinput[0] + "/ocred_" + splitedinput[1]

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
    cv2.imwrite(outputimage, img)
    cv2.waitKey(0)
    for i in result:
        print(i[1])

    # List 형식으로 저장되어 있는 결과를 json으로 변환
    LIST2JSON.tojson(result)


# import로 사용할 경우에는 이후 라인은 실행되지 않음. ModuleTest.py 참고
if __name__ == '__main__':
    PlayOCR("./testimg/demo.png")
