<template>
  <div id="home">
    <div id="orca-introduction" class="my-5">
      <h2>About ORCA</h2>
      <p>
        ORCA is a Korean OCR Software.<br>
        The existing OCR software were specialized in English and Number,
        so it's hard to recognize Korean accurately.<br>
        And finally, we made a new Korean OCR engine.
      </p>
    </div>
    <div id="team-introduction" class="my-10">
      <h2>About TEAM</h2>
      <p>
        <strong>Team AllDayLong</strong><br>
        : 하루종일 밤낮 가리지 않고 작업한다는 뜻
      <p>
        <strong>Members</strong><br>
        <ul>
          <li><strong>팀장</strong> 신병철 : Project Manage, AI Development</li>
          <li><strong>팀원</strong> 이기원 : AI Development, Back-end</li>
          <li><strong>팀원</strong> 황현섭 : Back-end</li>
          <li><strong>팀원</strong> 조진훈 : Front-end</li>
          <li><strong>팀원</strong> 조경서 : Front-end</li>
        </ul>
      </p>
    </div>
    <div id="practice-ocr" class="my-10">
      <h2>TEST</h2>
      <div id="ocr-container" class="pa-4">
        <p class="how_to_do_OCR">
          해당 위치에 사진을 드래그&드랍하거나 클릭하시면 이미지 업로드가 가능합니다.<br>
          하단의 샘플이미지를 선택하셔서 OCR을 체험하실 수 있습니다.
        </p>
        <img id="ocrLogo" src="../assets/image/TryOCR.png">
      </div>
      <div>
        <v-container id="sample-images" class="pa-4 my-10">
          <!-- 동적 그리드를 활용하여 하단에 샘플 사진 리스트 출력 -->
        </v-container>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  props: {
    msg: String
  }
}
</script>

<style>
  h2 {
    font-size: 1.5em;
  }
  ul {
    list-style: none;
  }
  #ocr-container {
    border: 3px solid lightskyblue;
    text-align: center;
  }
  #ocrLogo {
    height: 200px;
    width: 200px;
  }
  .how_to_do_OCR {
    color: green;
    font-size: 1.5em;
  }
  #sample-images {
    border: 3px solid lightskyblue;
    text-align: center;
  }
</style>
