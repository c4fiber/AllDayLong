<template>
  <div class="strength">
    <div class="intro">
      <h2>ORCA는 다른 OCR 모델과 다릅니다.</h2>
    </div>
    <hr><br>
    <!-- 학습 데이터 추가 -->
    <div class="addDataset">
      <div class="explanation">
        <h1>학습 데이터 추가</h1>
        <p>
        <ol>
          <li>네이버 CLOVA에서 제공하는 다양한 손글씨 폰트와 웹에서 제공하는 다양한 무료 폰트</li>
          <li>국립국어원에서 제공하는 한국어 사전을 이용하여 만든 딕셔너리 파일</li>
        </ol>
        </p>
        <p>
          위 두 자료를
          <a href="https://github.com/Belval/TextRecognitionDataGenerator">TextRecognitionDataGenerator(TRDG) 모듈</a>을 이용하여
          조합하여 학습용 데이터를 무작위로 350만개 생성하여 학습하였습니다.
        </p>
      </div>

      <div class="result">
        <h2>결과</h2>
        <table class="result1">
          <th>데이터 학습 전</th>
          <th>데이터 학습 후</th>
          <tr>
            <td><img id="beforeData" src="@/assets/image/BeforeDataAddition.jpg" alt="beforeData"></td>
            <td><img id="afterData" src="@/assets/image/AfterDataAddition.jpg" alt="aftereData"></td>
          </tr>
        </table>

        <table class="result2">
          <th class="inputData">Input Data</th>
          <th class="beforeData">데이터 추가 전</th>
          <th class="afterData">데이터 추가 후</th>
          <th class="confidence">인식 정확도<br>(추가 전 : 추가 후)</th>
          <tr class="가죽지의">
            <td><img id="input1" src="@/assets/image/가죽지의.png" alt="가죽지의"></td>
            <td class="fail">가족지의</td>
            <td>가죽지의</td>
            <td>0.8750 : 1.0000</td>
          </tr>
          <tr class="강렬하다">
            <td><img id="input2" src="@/assets/image/강렬하다.png" alt="강렬하다"></td>
            <td>강렬하다</td>
            <td>강렬하다</td>
            <td>0.6692 : 0.9995</td>
          </tr>
          <tr class="거절">
            <td><img id="input3" src="@/assets/image/거절.png" alt="거절"></td>
            <td>거절</td>
            <td>거절</td>
            <td class="astonish">0.2752 : 0.9993</td>
          </tr>
          <tr class="격식체">
            <td><img id="input4" src="@/assets/image/격식체.png" alt="격식체"></td>
            <td class="fail">적식체</td>
            <td>격식체</td>
            <td class="astonish">0.3239 : 0.9971</td>
          </tr>
          <tr class="고냉이똥">
            <td><img id="input5" src="@/assets/image/고냉이똥.png" alt="고냉이똥"></td>
            <td class="fail">고흙똥</td>
            <td class="fail">고냉이뚱</td>
            <td>0.1008 : 0.5869</td>
          </tr>
          <tr class="등전위점">
            <td><img id="input6" src="@/assets/image/등전위점.png" alt="등전위점"></td>
            <td class="fail">동전위점</td>
            <td>등전위점</td>
            <td>0.4785 : 0.9998</td>
          </tr>
          <tr class="사태막이">
            <td><img id="input7" src="@/assets/image/사태막이.png" alt="사태막이"></td>
            <td class="fail">사따이</td>
            <td>사태막이</td>
            <td class="astonish">0.1619 : 0.9988</td>
          </tr>
          <tr class="자미하다">
            <td><img id="input8" src="@/assets/image/자미하다.png" alt="자미하다"></td>
            <td>자미하다</td>
            <td>자미하다</td>
            <td>0.3372 : 1.0000</td>
          </tr>
        </table>
        <h3>
          데이터 학습 후 모델이 학습 전 모델보다 더 높은 인식 정확도를 보였습니다.<br>
          특히, 글자가 뚜렷하지 않거나, 글자의 간격이 좁은 경우 더 큰 차이를 보였습니다.
        </h3>
      </div>
    </div>
    <hr>

    <!-- 내부 알고리즘 개선 -->
    <div class="updateAlgorithm">
      <div class="explanation">
        <h1>내부 알고리즘 개선</h1>
        <img id="seq2seq" src="@/assets/image/seq2seq.jpg" alt="seq2seq">
        <p>
          기존 방식인 seq2seq(Sequence to Sequence) 방식은
          모델을 인코더(Encoder) 모듈과 디코더(Decoder) 모듈, 총 2개의 모듈로 나누어 수행합니다.
        </p>
        <p class="module-explanation">
          인코더(Encoder) 모듈 : 각 LSTM(CRNN)의 예측 결과를 벡터 데이터(Context Vector)로 압축하여 다음 LSTM(CRNN)에 전달<br>
          디코더(Decoder) 모듈 : 압축된 벡터 데이터(Context Vector)를 디코딩하여 문자 예측 후 출력
        </p>
        <p>
          여기서 각 LSTM(CRNN)은 바로 직전 LSTM(CRNN)의 예측 결과만을 입력 데이터로 받아 예측을 수행합니다.<br>
          따라서 디코더(Decoder) 모듈에는 인코더(Encoder) 모듈의 가장 마지막 LSTM(CRNN)만 예측에 영향을 끼칩니다.
        </p>
        <p>
        따라서, ORCA는 디코더(Decoder) 모듈의 매 예측 Step마다 인코더(Encoder) 모듈의 모든 LSTM(CRNN)의 예측 결과값을 참고하는
          <span>어텐션 메커니즘(Attention Mechanism)</span>을 적용하였습니다.
        </p>
        <img id="attn" src="@/assets/image/Attn.jpg" alt="Attention Mechanism">
      </div>

      <div class="result">
        <h2>결과</h2>
        <table class="result1">
          <th>Attn 적용 전</th>
          <th>Attn 적용 후</th>
          <tr>
            <td><img id="beforeAttn" src="@/assets/image/BeforeAttn.jpg" alt="beforeAttn"></td>
            <td><img id="afterAttn" src="@/assets/image/AfterAttn.jpg" alt="afterAttn"></td>
          </tr>
        </table>

        <table class="result2">
          <th>평균 수치</th>
          <th>Attn 적용 전</th>
          <th>Attn 적용 후</th>
          <tr>
            <td class="status">정확도(Accuracy)</td>
            <td>96.823</td>
            <td>96.778</td>
          </tr>
          <tr>
            <td class="status">소요시간(Elapsed_time)</td>
            <td class="shock">8,744s</td>
            <td class="shock">7,231s</td>
          </tr>
          <tr>
            <td class="status">Train Loss</td>
            <td>0.03427</td>
            <td>0.03925</td>
          </tr>
          <tr>
            <td class="status">Validation Loss</td>
            <td>0.05175</td>
            <td>0.05312</td>
          </tr>
        </table>

        <h3>
          어텐션 메커니즘(Attention Mechanism) 적용 전과 후의 정확도, Train Loss, Validation Loss 차이는 거의 없었지만,
          어텐션 메커니즘(Attention Mechanism) 적용 후의 소요시간은 적용 전의 소요시간 보다 <span>약 17.3%</span  > 감소하였습니다.
        </h3>
      </div>
    </div>
    <hr>
    <div class="end">
      <h2>따라서 <span>ORCA</span>는 많은 추가학습 데이터와 어텐션 메커니즘(Attention Mechanism)을 통해 기존 OCR 모델들보다 더 나은 성능을 가지고 있습니다.</h2>
    </div>
  </div>
</template>

<style>
  /* Font CSS */
  .strength {
    font-size: 1.3em;
  }
  h1, span {
    color: cornflowerblue;
  }
  span {
    font-weight: bold;
    font-style: italic;
  }
  .module-explanation {
    font-weight: bold;
    font-style: italic;
  }

  /* div CSS*/
  .addDataset, .updateAlgorithm {
    margin-bottom: 30px;
  }
  result {
    width: 100%;
  }
  .result > h2 {
    margin-top: 20px;
  }

  /* image CSS */
  #seq2seq, #attn {
    width: 70%;
    margin: 20px 0px;
  }
  #beforeData, #afterData, #beforeAttn, #afterAttn,
  #input1, #input2, #input3, #input4, #input5, #input6, #input7, #input8
  {
    width: 100%;
  }

  /* Table CSS */
  table, th ,tr, td {
    border: 2px solid black;
    border-collapse: collapse;
  }
  table {
    margin: 10px 0px 30px 0px;
    text-align: center;
    vertical-align: middle;
  }
  th {
    background: lightgrey;
  }
  .result2 {
    width: 90%;
  }
  .status {
    font-weight: bold;
    background-color: #f0f0f0;
  }
  td.fail {
    color: red;
  }
  td.astonish {
    color: blue;
  }
  td.shock {
    color: red;
    font-weight: bold;
  }
</style>
