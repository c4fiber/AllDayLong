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
          <li><strong>팀장</strong> 신병철 : Project Manager, AI Model Developer</li>
          <li><strong>팀원</strong> 이기원 : AI Model Developer, Back-end Developer</li>
          <li><strong>팀원</strong> 황현섭 : Back-end Developer</li>
          <li><strong>팀원</strong> 조진훈 : Front-end Developer</li>
          <li><strong>팀원</strong> 조경서 : Front-end Developer</li>
        </ul>
      </p>
    </div>
    <div id="practice-ocr" class="my-10">
      <h2>TEST</h2>

      <!-- 샘플 리스트 container -->
      <div class="pa-4">
        <v-container id="sample-images">
          OCR 샘플 이미지 파일들을 display할 Grid<br>
          동적 그리드 활용
        </v-container>
      </div>

      <!-- 실제 TEST container -->
      <div id="testOCR" class="pa-4">
        <form @change="onFileSelected">
          <v-container id="add-image">
            <input id="file-input" type="file" style="display: none">
            <label for="file-input">

              <!-- 성공한 버전 -->
              <div id="img-container" class="drop-zone" style="padding: 20px">
                <p class="how_to_do_OCR">
                  해당 화면을 클릭하거나 해당 위치에 사진을 Drag & Drop 하시면 이미지 업로드가 가능합니다.<br>
                  상단의 샘플이미지를 선택하셔서 OCR을 체험하실 수 있습니다.
                </p>
                <img id="ocrLogo" src="../assets/image/TryOCR.png">
              </div>

<!--              &lt;!&ndash; 현재 통합중인 Drag & Drop 기능 추가버전 &ndash;&gt;-->
<!--              <div id="img-container">-->
<!--                <picture-input-->
<!--                  ref="pictureInput"-->
<!--                  width="600"-->
<!--                  height="600"-->
<!--                  margin="16"-->
<!--                  accept="image/jpeg,image/png"-->
<!--                  size="10"-->
<!--                  button-class="btn"-->
<!--                  :custom-strings="{-->
<!--                  upload: '<h1>Bummer!</h1>',-->
<!--                  drag: '해당 화면을 클릭하거나<br>사진을 Drag&Drop 하세요.'-->
<!--                }"-->
<!--                  @change="onChange">-->
<!--                </picture-input>-->
<!--              </div>-->
            </label>
            </input>
          </v-container>
          <v-container id="submit-btn">
            <input type="submit" value="Submit(임시) - 최종적으로는 해당버튼 삭제예정" @click="onUpload"/>
          </v-container>
        </form>
      </div>

      <!-- OCR 결과 출력 -->
      <div class="pa-4">
        <v-container id="showResult">
          OCR 결과(JSON) 출력 Container
        </v-container>
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios';
import PictureInput from 'vue-picture-input'

export default {
  name: 'HomeView',
  props: {
    msg: String
  },

  data(){
    return{
      selectedFile:null
    };
  },
  components: {
    PictureInput
  },
  methods:{
    onFileSelected(event){
      this.selectedFile=event.target.files[0]
    },
    onUpload(){
      var fd = new FormData();
      fd.append('file',this.selectedFile)
      axios.post('http://localhost:3000/upload',fd)
        .then(res =>{
          console.log(res)
        });
    },
    onChange () {
      console.log('New picture selected!')
      if (this.$refs.pictureInput.image) {
        console.log('Picture loaded.')
      } else {
        console.log('FileReader API not supported: use the <form>, Luke!')
      }
    }
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
  #img-container {
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
  #sample-images, #submit-btn, #showResult {
    border: 3px solid lightskyblue;
    text-align: center;
  }
</style>
