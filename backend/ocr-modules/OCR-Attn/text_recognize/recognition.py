import os
import string
import argparse
from loguru import logger

import torch
import torch.backends.cudnn as cudnn
import torch.utils.data
import torch.nn.functional as F

from text_recognize.utils import CTCLabelConverter, AttnLabelConverter
from text_recognize.dataset import RawDataset, AlignCollate
from text_recognize.model import Model


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


class Recognition:
    def __init__(
        self,
        image_folder,
        saved_model,
        Transformation,
        FeatureExtraction,
        SequenceModeling,
        Prediction,
        workers=0,
        batch_size=192,
        batch_max_length=25,
        imgH=32,
        imgW=100,
        rgb=False,
        character=" !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~가각간갇갈감갑값강갖같갚갛개객걀거걱건걷걸검겁것겉게겨격겪견결겹경곁계고곡곤곧골곰곱곳공과관광괜괴굉교구국군굳굴굵굶굽궁권귀규균그극근글긁금급긋긍기긴길김깅깊까깎깐깔깜깝깥깨꺼꺾껍껏껑께껴꼬꼭꼴꼼꼽꽂꽃꽉꽤꾸꿀꿈뀌끄끈끊끌끓끔끗끝끼낌나낙낚난날낡남납낫낭낮낯낱낳내냄냉냐냥너넉널넓넘넣네넥넷녀녁년념녕노녹논놀놈농높놓놔뇌뇨누눈눕뉘뉴늄느늑는늘늙능늦늬니닐님다닥닦단닫달닭닮담답닷당닿대댁댐더덕던덜덤덥덧덩덮데델도독돈돌돕동돼되된두둑둘둠둡둥뒤뒷드득든듣들듬듭듯등디딩딪따딱딴딸땀땅때땜떠떡떤떨떻떼또똑뚜뚫뚱뛰뜨뜩뜯뜰뜻띄라락란람랍랑랗래랜램랫략량러럭런럴럼럽럿렁렇레렉렌려력련렬렵령례로록론롬롭롯료루룩룹룻뤄류륙률륭르른름릇릎리릭린림립릿마막만많말맑맘맙맛망맞맡맣매맥맨맵맺머먹먼멀멈멋멍멎메멘멩며면멸명몇모목몰몸몹못몽묘무묵묶문묻물뭄뭇뭐뭣므미민믿밀밉밌및밑바박밖반받발밝밟밤밥방밭배백뱀뱃뱉버번벌범법벗베벤벼벽변별볍병볕보복볶본볼봄봇봉뵈뵙부북분불붉붐붓붕붙뷰브블비빌빗빚빛빠빨빵빼뺨뻐뻔뻗뼈뽑뿌뿐쁘쁨사삭산살삶삼상새색샌생서석섞선설섬섭섯성세센셈셋션소속손솔솜솟송솥쇄쇠쇼수숙순술숨숫숲쉬쉽슈스슨슬슴습슷승시식신싣실싫심십싱싶싸싹쌀쌍쌓써썩썰썹쎄쏘쏟쑤쓰쓸씀씌씨씩씬씹씻아악안앉않알앓암압앗앙앞애액야약얇양얗얘어억언얹얻얼엄업없엇엉엌엎에엔엘여역연열엷염엽엿영옆예옛오옥온올옮옳옷와완왕왜왠외왼요욕용우욱운울움웃웅워원월웨웬위윗유육율으윽은을음응의이익인일읽잃임입잇있잊잎자작잔잖잘잠잡장잦재쟁저적전절젊점접젓정젖제젠젯져조족존졸좀좁종좋좌죄주죽준줄줌줍중쥐즈즉즌즐즘증지직진질짐집짓징짙짚짜짝짧째쨌쩌쩍쩐쪽쫓쭈쭉찌찍찢차착찬찮찰참창찾채책챔챙처척천철첫청체쳐초촉촌총촬최추축춘출춤춥춧충취츠측츰층치칙친칠침칭카칸칼캐캠커컨컬컴컵컷켓켜코콜콤콩쾌쿠퀴크큰클큼키킬타탁탄탈탑탓탕태택탤터턱털텅테텍텔템토톤톱통퇴투툼퉁튀튜트특튼튿틀틈티틱팀팅파팎판팔패팩팬퍼퍽페펴편펼평폐포폭표푸푹풀품풍퓨프플픔피픽필핏핑하학한할함합항해핵핸햄햇행향허헌험헤헬혀현혈협형혜호혹혼홀홍화확환활황회획횟효후훈훌훔훨휘휴흉흐흑흔흘흙흡흥흩희흰히힘",
        sensitive=False,
        PAD=False,
        num_fiducial=20,
        input_channel=1,
        output_channel=256,
        hidden_size=256,
    ):
        self.image_folder = image_folder
        self.saved_model = saved_model
        self.Transformation = Transformation
        self.FeatureExtraction = FeatureExtraction
        self.SequenceModeling = SequenceModeling
        self.Prediction = Prediction
        self.workers = workers
        self.batch_size = batch_size
        self.batch_max_length = batch_max_length
        self.imgH = imgH
        self.imgW = imgW
        self.rgb = rgb
        self.character = character
        self.sensitive = sensitive
        self.PAD = PAD
        self.num_fiducial = num_fiducial
        self.input_channel = input_channel
        self.output_channel = output_channel
        self.hidden_size = hidden_size

        """ vocab / character number configuration """
        if self.sensitive:
            self.character = string.printable[:-6]  # same with ASTER setting (use 94 char).

        cudnn.benchmark = True
        cudnn.deterministic = True
        self.num_gpu = torch.cuda.device_count()

        self.__loadNet()

    def __loadNet(self):
        if "CTC" in self.Prediction:
            self.converter = CTCLabelConverter(self.character)
        else:
            self.converter = AttnLabelConverter(self.character)
        self.num_class = len(self.converter.character)

        if self.rgb:
            self.input_channel = 3
        model = Model(self)
        logger.info(
            "model input parameters {} {} {} {} {} {} {} {} {} {} {} {}".format(
                self.imgH,
                self.imgW,
                self.num_fiducial,
                self.input_channel,
                self.output_channel,
                self.hidden_size,
                self.num_class,
                self.batch_max_length,
                self.Transformation,
                self.FeatureExtraction,
                self.SequenceModeling,
                self.Prediction,
            )
        )
        self.model = torch.nn.DataParallel(model).to(device)
        # load model
        print("loading pretrained model from %s" % self.saved_model)
        self.model.load_state_dict(torch.load(self.saved_model, map_location=device))
        self.model.eval()
        logger.info("Model loaded")

    def TextRecognize(self):
        results = {}
        logger.info("Loading image boxes")
        # prepare data. two demo images from https://github.com/bgshih/crnn#run-demo
        AlignCollate_demo = AlignCollate(
            imgH=self.imgH, imgW=self.imgW, keep_ratio_with_pad=self.PAD
        )
        demo_data = RawDataset(root=self.image_folder, opt=self)  # use RawDataset
        demo_loader = torch.utils.data.DataLoader(
            demo_data,
            batch_size=self.batch_size,
            shuffle=False,
            num_workers=int(self.workers),
            collate_fn=AlignCollate_demo,
            pin_memory=True,
        )

        with torch.no_grad():
            for image_tensors, image_path_list in demo_loader:
                batch_size = image_tensors.size(0)
                image = image_tensors.to(device)
                # For max length prediction
                length_for_pred = torch.IntTensor([self.batch_max_length] * batch_size).to(device)
                text_for_pred = (
                    torch.LongTensor(batch_size, self.batch_max_length + 1).fill_(0).to(device)
                )

                if "CTC" in self.Prediction:
                    preds = self.model(image, text_for_pred)

                    # Select max probabilty (greedy decoding) then decode index to character
                    preds_size = torch.IntTensor([preds.size(1)] * batch_size)
                    _, preds_index = preds.max(2)
                    preds_index = preds_index.view(-1)
                    preds_str = self.converter.decode(preds_index.data, preds_size.data)

                else:
                    preds = self.model(image, text_for_pred, is_train=False)

                    # select max probabilty (greedy decoding) then decode index to character
                    _, preds_index = preds.max(2)
                    preds_str = self.converter.decode(preds_index, length_for_pred)

                # dashed_line = "-" * 80
                # head = f'{"image_path":25s}\t{"predicted_labels":25s}\tconfidence score'

                # print(f"{dashed_line}\n{head}\n{dashed_line}")

                preds_prob = F.softmax(preds, dim=2)
                preds_max_prob, _ = preds_prob.max(dim=2)
                for img_name, pred, pred_max_prob in zip(
                    image_path_list, preds_str, preds_max_prob
                ):
                    if "Attn" in self.Prediction:
                        pred_EOS = pred.find("[s]")
                        pred = pred[:pred_EOS]  # prune after "end of sentence" token ([s])
                        pred_max_prob = pred_max_prob[:pred_EOS]

                    # calculate confidence score (= multiply of pred_max_prob)
                    confidence_score = pred_max_prob.cumprod(dim=0)[-1]
                    results[img_name] = {
                        "predicted_labels": pred,
                        "confidence_score": float(confidence_score),
                    }
                    # remove processed img
                    os.remove(img_name)
                    # print(f"{img_name:25s}\t{pred:25s}\t{confidence_score:0.4f}")
        try:
            logger.info(f"{img_name.split('_box_')[0]} recognized, total {len(results)}")
        except:
            logger.warning("No image boxes")
        return results


if __name__ == "__main__":
    path_abs = os.path.dirname(os.path.abspath(__file__))
    test = Recognition(
        image_folder=f"{path_abs}/../images/",
        saved_model=f"{path_abs}/TPS-ResNet-BiLSTM-Attn.pth",
        Transformation="TPS",
        FeatureExtraction="ResNet",
        SequenceModeling="BiLSTM",
        Prediction="Attn",
    )
    result = test.TextRecognize()
    print(result)
