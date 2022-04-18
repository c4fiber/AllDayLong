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

    for i in result:
        x = i[0][0][0]
        y = i[0][0][1]
        w = i[0][1][0] - i[0][0][0]
        h = i[0][2][1] - i[0][1][1]

        color_idx = random.randint(0, 255)
        color = [int(c) for c in COLORS[color_idx]]
        img = cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)

    # save image
    cv2.imwrite(output_path, img)
