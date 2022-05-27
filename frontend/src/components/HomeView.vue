<template>
  <div id="home">
    <!-- 실제 TEST container -->
    <div id="practice-ocr" class="my-10">
      <h2>TEST</h2>

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
            }"
            @change="onChange">
        </picture-input>
      </div>

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
            <img :src=imageurl alt="imageOCR"/>
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

  data(){
    return{
      selectedFile:null,
      ocrtext: [],
      images:[]
    };
  },
  components: {
    PictureInput
  },
  created() {
    
  },
  methods:{
    onFileSelected(event){
      this.selectedFile=event.target.files[0]
    },
    onUpload(){
      var fd = new FormData();
      fd.append('file',this.selectedFile)
      axios.post('http://localhost:3000/upload',fd)
        .then(this.test());
    },
    onChange () {
      console.log('New picture selected!')
      if (this.$refs.pictureInput.image) {
        console.log('Picture loaded.')
      } else {
        console.log('FileReader API not supported: use the <form>')
      }
    },
    test(){
      this.timerfunc=setInterval(() =>{
            this.$http.get('/api/upload')
            .then((res) => {
            this.ocrtext = res.data.test;
            this.images=res.data.test2;
            if(this.images[0]!=null){
                clearInterval(this.timerfunc);
                if(this.ocrtext[0]==null){
                this.ocrtext[0]="No Text";
                }

            }
            })
            .catch((err) => {
            console.error(err);
            });
        	 },3000);
    }
  }
}
</script>

<style>
  h2 {
    font-size: 1.5em;
  }
  ul {
    color: rgba(0, 0, 0, 0.65); // 추가된 부분
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
