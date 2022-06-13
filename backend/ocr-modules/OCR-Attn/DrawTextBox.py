import numpy as np
import random
import cv2
import os


def Draw(image, result):
    #  output 저장을 위한 경로 설정
    output_path = os.path.dirname(image) + "/ocred_" + os.path.basename(image)

    #  Draw TextBox with opencv
    img = cv2.imread(image)
    np.random.seed(42)
    COLORS = np.random.randint(0, 255, size=(255, 3), dtype="uint8")

    for i in range(len(result['text'])):
        y1 = result['text'][i]['location'][0]
        y2 = result['text'][i]['location'][1]
        x1 = result['text'][i]['location'][2]
        x2 = result['text'][i]['location'][3]

        color_idx = random.randint(0, 254)
        color = [int(c) for c in COLORS[color_idx]]
        img = cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

    # save image
    cv2.imwrite(output_path, img)
