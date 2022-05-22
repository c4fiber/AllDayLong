<template>
  <div id="home">
    <div id="orca-introduction" class="my-5">
      <h2>About ORCA</h2>
      <p id="InText">
        ORCA is a Korean OCR Software.<br>
        The existing OCR software were specialized in English and Number,
        so it's hard to recognize Korean accurately.<br>
        And finally, we made a new Korean OCR engine.
      </p>
    </div>

    <div id="team-introduction" class="my-10">
      <h2>About TEAM</h2>
        <strong>Team AllDayLong</strong><br>
      <p id="InText">
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
      <h2>Try OCRA by your image</h2>
      <p id="InText"> Select image from your device and submit.</p>

      <!-- 샘플 리스트 container -->
      <div class="pa-4">
        <v-container id="sample-images" >
          <div><img id="OcrSampleImages" src="" alt="ocr example"></div>
        </v-container>
      </div>

      <!-- 실제 TEST container -->
      <div id="testOCR" class="pa-4">
        <form @change="onFileSelected">
          <!-- mobile 버전 -->
          <mq-layout :mq="['sm', 'md']">
          <v-container id="add-image">
            <input id="file-input" type="file" style="display: none">
            <label for="file-input">

              <div class="mdi mdi-file-image-plus" id="img-container" style="padding: 10px"> image select</div>
            </label>
            </input>
          </v-container>
          </mq-layout>

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
  input[type="file"] {
    cursor: pointer;
  }
  h2 {
    font-size: 1.5em;
  }
  strong {
    color: rgba(0, 0, 0, 1);
  }
  ul {
    color: rgba(0, 0, 0, 0.65);
    list-style: none;
  }
  #img-container {
    border: 1px solid black;
    border-radius: 4px;
    text-align: center;
    width : 90%;
    margin : 0 auto;
  }

  #ocrLogo {
    height: 200px;
    width: 200px;
  }
  .how_to_do_OCR {
    color: green;
    font-size: 1.5em;
  }
  #submit-btn, #showResult {
    border: 1px solid black;
    height: 300px;
    border-radius:4px;
    text-align: center;
  }
  #sample-images {
    border: 1px solid black;
    width : 90%;
    border-radius:4px;
    margin: 0 auto;
  }
  #OcrSampleImages{
    padding-top: 56.25%;
  }
  #showResult{
    width: 90%;
  }
  #InText{
    color: rgba(0, 0, 0, 0.65);
    margin-left: 10px;
  }
</style>