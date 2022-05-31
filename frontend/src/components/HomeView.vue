<template>
  <div id="home">
    <!-- About 소개 -->
    <!-- AboutView.vue(About 메뉴)로 이동하는 것을 고려 중 -->
    <!-- <div id="orca-introduction" class="my-5">
      <h2>About ORCA</h2>
      <p id="InText">
        ORCA is a Korean OCR Software.<br>
        The existing OCR software were specialized in English and Number,
        so it's hard to recognize Korean accurately.<br>
        And finally, we made a new Korean OCR engine.
      </p>
    </div> -->

    <!-- 팀 소개 -->
    <!-- 기존에 생성된 UserAll.vue(Developers 메뉴)에 이동하는 것을 고려중
          (이에 추가로 내부 코드를 수정하여 아래의 내용을 해당 컴포넌트에 띄우는 것을 고려) -->
    <!-- <div id="team-introduction" class="my-10">
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
    </div> -->

    <!-- 실제 TEST container -->
    <div id="practice-ocr" class="my-10">
      <h2>Try ORCA by your image</h2>
      <p id="InText"> Select image from your device and submit.</p>

    <!-- Drag&Drop 기능 구현된 PC버전 -->
    <mq-layout :mq="['lg']">
      <div id="img-container-pc" class="pa-10 my-5" @change="onFileSelected">
        <picture-input
          ref="pictureInput"
          width="800"
          height="800"
          accept="image/jpeg,image/png"
          hideChangeButton="true"
          button-class="btn"
          :custom-strings="{
            upload: '<p>업로드를 지원하지 않는 기기입니다.</p>',
            drag: '해당 화면을 클릭하거나<br>사진을 Drag&Drop 하세요.'
          }" @change="onChange">
        </picture-input>
      </div>
    </mq-layout>

    <!-- 모바일 버전 -->
    <mq-layout :mq="['sm', 'md']">
      <div id="img-container-mobile" class=" my-4">
        <form @change="onFileSelected">
          <input id="file-input" type="file" style="display: none">
          <label for="file-input">
            <div class="mdi mdi-file-image-plus" id="img-container" style="padding: 10px">Image select...</div>
          </label>
          </input>
        </form>
      </div>
    </mq-layout>

    <!-- Submit 버튼 -->
    <div class="mdi mdi-file-upload-outline" id="submit-btn" style="padding:10px">
      <input type="submit" value="Submit" @click="onUpload">
    </div>

    <div id="practice-ocr" class="my-10">
      <h2>Result</h2>
      <p id="InText">Check the results using orca</p>
    </div>
    <!-- OCR 결과 출력 -->
    <div id=showResult class="pa-4 my-5">
      <div class="ocrtext">
        <div v-for="(text, index) in ocrtext" :key="index" class="user">

          <p>{{ text }} </p><br>
        </div>
      </div>

      <div class="images">
        <br>
        <div v-for="(imageurl, index2) in images" :key="index2" class="image">
          <img :src=imageurl alt="imageOCR" />
        </div>
      </div>
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

    data() {
      return {
        selectedFile: null,
        ocrtext: [],
        images: []
      };
    },
    components: {
      PictureInput
    },
    created() {
      this.$http.get('/api/upload')
        .then((res) => {
          this.ocrtext = res.data.test;
          this.images = res.data.test2;
        })
        .catch((err) => {
          console.error(err);
        });
    },
    methods: {
      onFileSelected(event) {
        this.selectedFile = event.target.files[0]
      },
      onUpload() {
        var fd = new FormData();
        fd.append('file', this.selectedFile)
        axios.post('http://localhost:3000/upload', fd)
          .then(res => {
            console.log(res)
          });
      },
      onChange() {
        console.log('New picture selected!')
        if (this.$refs.pictureInput.image) {
          console.log('Picture loaded.')
        } else {
          console.log('FileReader API not supported: use the <form>')
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
    color: rgba(0, 0, 0, 0.65);
    list-style: none;
  }

  input[type="file"] {
    cursor: pointer;
  }
  
  /* 입력 & 출력 div */
  /* 기존 버전 */
  #img-container-pc,
  #showResult {
    border: 3px solid #87cefa;
    text-align: center;
  }

  /* 입력 버전 */
  #img-container-mobile {
    border: 1px solid black;
    border-radius: 4px;
    text-align: center;
    width: 90%;
    margin: 0 auto;
    height: 46.5px;
  }

  #submit-btn {
    border: 1px solid black;
    height: 46.5px;
    border-radius: 4px;
    text-align: center;
    width: 90%;
    margin: 0 auto;
  }

  #showResult {
    border: 1px solid black;
    width: 90%;
    margin: 0 auto;
    border-radius: 4px;
    text-align: left;
  }

  #InText {
    color: rgba(0, 0, 0, 0.65);
    margin-left: 10px;
  }

  /* 공통(기존, input) 부분 */
  #ocrLogo {
    height: 200px;
    width: 200px;
  }

  .how_to_do_OCR {
    color: green;
    font-size: 1.5em;
  }

  /* 출력 div */
  .user {
    float: left;
    border: 2px solid black;
    padding: 15px;
    margin: 20px;
  }

  .image {
    float: left;
    border: 2px solid black;
    padding: 15px;
    margin: 20px;
  }

</style>
