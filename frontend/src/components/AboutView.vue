<template>
  <div class="about">
    <!-- OCR 개념 -->
    <div class="aboutOCR">
      <h1>About OCR</h1>
      <p>
        : OCR(Optical Character Recognition)은 이미지 파일 속 텍스트를 실제 문자 텍스트 형태로 변환시키는 기술입니다.<br>
        문자 탐지(Text Detection) 단계와 문자 인식(Text Recognition) 단계로 구성되어 있습니다.
      </p>
    </div>
   <div class="OCRimg">
     <img id="OCR" src="@/assets/image/OCR.png" alt="OCR">
   </div>

    <!-- OCR 관련 주요 기술 -->
    <div class="existingOCR">
      <h1>Existing OCR SW</h1>

      <div class="globalOCR">
        <h2>Tesseract OCR, Easy OCR</h2>
        <p>
          : 세계적으로 많이 사용되는 오픈소스 OCR 모델
        </p>
        <p class="problem">
          : 영어와 숫자 인식을 중점으로 개발되어 한국어의 인식률이 매우 저조
        </p>
        <img id="TesseractOCR" src="@/assets/image/TesseractOCR.png" alt="TesseractOCR">
        <img id="EasyOCR" src="@/assets/image/EasyOCR.png" alt="EasyOCR">
      </div>

      <div class="koreanOCR">
        <h2>CLOVA OCR, SynapSoft OCR</h2>
        <p>
          : 높은 수준의 한국어 인식률을 보유한 OCR 모델
        </p>
        <p class="problem">
          : 접근성이 낮음<br>
          : (CLOVA) 개발자를 대상으로 서비스 제공, 비용 지출 요구
        </p>
        <img id="ClovaOCR" src="@/assets/image/ClovaOCR.png" alt="ClovaOCR">
        <img id="SynapOCR" src="@/assets/image/SynapOCR.png" alt="SynapOCR">
        <br><br>
        <h3>그래서 저희는 위의 문제점(한국어 인식률, 접근성, 비용)을 개선한 새로운 OCR SW인 <span>ORCA</span>를 개발했습니다.</h3>
      </div>
    </div>

    <!-- 사용 Tools -->
      <div class="usedTools">
        <h1>Used Tools</h1>
        <table>
          <th class="part">파트</th>
          <th colspan="2">사용 Tool</th>
          <tr class="UI">
            <td class="part">사용자 인터페이스</td>
            <td>Vue.js</td>
            <td class="img"><img id="Vue" src="@/assets/image/Vue.png" alt="Vue"></td>
          </tr>
          <tr class="server">
            <td class="part">웹 서버</td>
            <td>node.js Express</td>
            <td class="img"><img id="nodeExpress" src="@/assets/image/nodeExpress.png" alt="nodeExpress"></td>
          </tr>
          <tr class="database">
            <td class="part">데이터베이스</td>
            <td>mongoDB</td>
            <td class="img"><img id="mongoDB" src="@/assets/image/mongoDB.png" alt="mongoDB"></td>
          </tr>
          <tr class="machine-learning">
            <td class="part">머신러닝</td>
            <td>Pytorch</td>
            <td class="img"><img id="Pytorch" src="@/assets/image/Pytorch.png" alt="Pytorch"></td>
          </tr>
        </table>
      </div>
  </div>
</template>
<style>
  /* Font CSS */
  .about {
    font-size: 1.3em;
  }
  h1, span {
    color: cornflowerblue;
  }
  span {
    font-weight: bold;
    font-style: italic;
  }
  .problem {
    color: red;
    font-weight: bold;
  }

  /* div CSS */
  .aboutOCR, .existingOCR, .globalOCR, .koreanOCR, .usedTools {
    float: left;
  }
  .OCRimg {
    float: right;
    width: 30%;
    margin-top: 10px;
  }
  .aboutOCR {
    width: 70%;
  }
  .existingOCR {
    clear: both;
  }
  .globalOCR, .koreanOCR{
    margin-bottom: 20px;
  }
  .usedTools {
    margin-top: 20px;
  }

  /* image CSS */
  #TesseractOCR, #EasyOCR, #ClovaOCR, #SynapOCR {
    margin: 0px 20px 20px 20px;
  }
  #Vue, #nodeExpress, #mongoDB, #Pytorch {
    width: 30%;
    height: 50%;
  }

  /* Table CSS */
  table, th, tr, td {
    border: 3px solid black;
    border-collapse: collapse;
  }
  table {
    margin: 10px 0px 30px 0px;
    text-align: center;
  }
  th.part {
    width: 20%;
  }
  td.part {
    font-weight: bold;
  }
  td.img {
    width: 60%;
  }
</style>
