import os
import sys
import LIST2JSON
import DrawTextBox
from ocr import OCR
from types import SimpleNamespace


def OCREngine(image):
    # 이하 opt을 변경하여 기학습된 모델을 교체할 수 있음
    #  Parameters가 변경되었을 경우 OCR-Attn/text_recognize/recognition.py을 참조할 것.

    path_abs = os.path.dirname(os.path.abspath(__file__))
    opt = SimpleNamespace()
    opt.detect_trained_model = f"{path_abs}/models/craft_mlt_25k.pth"
    opt.detect_result_folder = f"{path_abs}/images/box/"
    opt.recognize_image_folder = f"{path_abs}/images/box/"
    opt.recognize_saved_model = f"{path_abs}/models/TPS-VGG-BiLSTM-Attn.pth"
    opt.recognize_Transformation = "TPS"
    opt.recognize_FeatureExtraction = "VGG"
    opt.recognize_SequenceModeling = "BiLSTM"
    opt.recognize_Prediction = "Attn"

    start = OCR(opt)
    result = start.run(image)

    print(result)
    json_path = os.path.dirname(image) + "/" + os.path.basename(image) + ".json"
    LIST2JSON.tojson(result, json_path)
    DrawTextBox.Draw(image, result)


if __name__ == '__main__':
    image_path = sys.argv[1]  # 명령행 인자
    OCREngine(image_path)
    # OCREngine('C:/Users/Fair/PycharmProjects/Module/OCR-Attn/test/demo.png')
