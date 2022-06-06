<template>
  <div class="about">
    <h2>OCR Introduction</h2>
    <p>
      OCR(Optical Character Recognition)은 이미지 속의 텍스트를 실제 문자 텍스트 형태로 변환시키는 기술이다. Text Detection 단계와 Text Recognition 단계로
      구성되어 있다.
      대표적인 OCR 엔진으로는 EasyOCR, Tesseract OCR이 있다.
    </p>
    <h2>Related OCR Technology Status</h2>
      <h4><span style="color:#009dff;">Tesseract OCR</span></h4>
    <p>
      특징: HP 연구소에서 개발한 오픈소스 OCR, 높은 정확도
      문제점: 한글 인식률이 저조, 자체적인 인식률 개선에 한계가 존재
    </p>
      <h4><span style="color:#2db245;">NAVER CLOVA</span></h4>
    <p>
      특징: 배열된 문자와 읽는 순서를 이용하여 AI 모델을 바탕으로 인식
      문제점: 지속적인 비용 지불, 개발자를 대상으로 하는 서비스로 접근성이 낮음
    </p>
    <h2>Development Background</h2>
    <p>
      영어 위주의 OCR 기술은 한글의 인식률이 저조하고, 개발자 위주의 서비스를 하여 접근성이 떨어지는 단점들이 존재한다.
    </p>
    <h2>Then what is <span style="color:#3cb1f9;">ORCA</span></h2>
    <p>
      <span style="color:#3cb1f9;">ORCA</span>는 위에 나열한 문제점들을 보완하여 누구나 쉽게 체험 가능한 한국어 OCR 모델이다.
    </p>
    <!-- <p>
      <span style="color:#3cb1f9;">ORCA</span>는 기존의 OCR 모델이 영어와 숫자에 중점을 두고, 한글의 경우 인쇄글자와 문서에만 서비스를 제공하며 그마저도 인식 정확도가 낮은 문제점들을 보완, 개선한 새로운 한국어 OCR 모델이다.
    </p> -->
    <h2>Applied OCR model</h2>
    <p>
      ORCA은 기존 OCR 데이터의 특징을 추출하여 패턴을 파악하는 CNN(Convolution Neural Network)과 이전 단계의 학습 데이터를 현재 학습에 반영시키는 RNN(Recurrent
      Neural Network)을 합친
    </p>
    <h2>사용 TOOLS</h2> 
    <img id = "Tool_img" src="@/assets/image/Applied_Tool.png" alt="">
  </div>
</template>
<style>
  p{
    color: rgba(0, 0, 0, 0.8);
  }
  #Tool_img{
    width: 60%;
    height: 300px;
    margin: 0 20%;
}
</style>
