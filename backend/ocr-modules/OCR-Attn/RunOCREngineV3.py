import os
import sys
import LIST2JSON
import DrawTextBox
from ocr import OCR
from types import SimpleNamespace
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="torch.nn.functional")


def OCREngine(image):
    # 이하 opt을 변경하여 기학습된 모델을 교체할 수 있음
    #  Parameters가 변경되었을 경우 OCR-Attn/text_recognize/recognition.py을 참조할 것.

    # 1차 모델 TPS-VGG-BiLSTM-Attn
    path_abs = os.path.dirname(os.path.abspath(__file__))
    opt = SimpleNamespace()
    opt.detect_trained_model = f"{path_abs}/models/craft_mlt_25k.pth"
    opt.detect_result_folder = f"{path_abs}/images/box/"
    opt.recognize_image_folder = f"{path_abs}/images/box/"
    opt.recognize_saved_model = f"{path_abs}/3split_saved_models/3split_ocr.pth"
    opt.recognize_Transformation = "TPS"
    opt.recognize_FeatureExtraction = "VGG"
    opt.recognize_SequenceModeling = "BiLSTM"
    opt.recognize_Prediction = "Attn"
    # 2차 모델 TPS-VGG-BiLSTM-Attn
    path_abs = os.path.dirname(os.path.abspath(__file__))
    opt2 = SimpleNamespace()
    opt2.detect_trained_model = f"{path_abs}/models/craft_mlt_25k.pth"
    opt2.detect_result_folder = f"{path_abs}/images/box/"
    opt2.recognize_image_folder = f"{path_abs}/images/box/"
    opt2.recognize_saved_model = f"{path_abs}/3split_saved_models/3split_htr.pth"
    opt2.recognize_Transformation = "TPS"
    opt2.recognize_FeatureExtraction = "VGG"
    opt2.recognize_SequenceModeling = "BiLSTM"
    opt2.recognize_Prediction = "Attn"
    # 3차 모델 None-VGG-BiLSTM-CTC
    path_abs = os.path.dirname(os.path.abspath(__file__))
    opt3 = SimpleNamespace()
    opt3.detect_trained_model = f"{path_abs}/models/craft_mlt_25k.pth"
    opt3.detect_result_folder = f"{path_abs}/images/box/"
    opt3.recognize_image_folder = f"{path_abs}/images/box/"
    opt3.recognize_saved_model = f"{path_abs}/3split_saved_models/3split_korean_g2.pth"
    opt3.recognize_Transformation = "None"
    opt3.recognize_FeatureExtraction = "VGG"
    opt3.recognize_SequenceModeling = "BiLSTM"
    opt3.recognize_Prediction = "CTC"

    # OCR
    start = OCR(opt)
    result1 = start.run(image)
    print("#Model 1:", opt.detect_trained_model,
          "\n Network Model :", opt.recognize_Transformation, opt.recognize_FeatureExtraction,
          opt.recognize_SequenceModeling, opt.recognize_Prediction,
          "\n Results :\n", result1)

    start = OCR(opt2)
    result2 = start.run(image)
    print("#Model 2:", opt2.detect_trained_model,
          "\n Network Model :", opt2.recognize_Transformation, opt2.recognize_FeatureExtraction,
          opt2.recognize_SequenceModeling, opt2.recognize_Prediction,
          "\n Results :\n", result2)

    start = OCR(opt3)
    result3 = start.run(image)
    print("#Model 3:", opt3.detect_trained_model,
          "\n Network Model :", opt3.recognize_Transformation, opt3.recognize_FeatureExtraction,
          opt3.recognize_SequenceModeling, opt3.recognize_Prediction,
          "\n Results :\n", result3)

    # OCR 결과 변환
    json_path = os.path.dirname(image) + "/" + os.path.basename(image) + ".json"
    LIST2JSON.tojsontrio(result1, result2, result3, json_path)
    DrawTextBox.Draw(image, result1)


if __name__ == '__main__':
    # image_path = sys.argv[1]  # 명령행 인자
    # OCREngine(image_path)
    OCREngine('C:/Users/Fair/PycharmProjects/Module/OCR-Attn/test/demo.png')
