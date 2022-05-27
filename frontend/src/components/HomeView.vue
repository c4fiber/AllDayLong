<template>
  <div id="home">
    <!-- PC버전 (with Drag & Drop) -->
    <mq-layout :mq="['lg']">
      <h1>TEST</h1>
      <div id="img-container-pc" class="py-5 mt-2 mb-6" @change="onFileSelected">
        <picture-input
          ref="pictureInput"
          width="800"
          height="600"
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
    </mq-layout>

    <!-- 모바일 버전 (with Click) -->
    <mq-layout :mq="['sm', 'md']">
      <h1 class="pl-3">TEST</h1>
      <div id="img-container-mobile" class="mt-2 mb-6">
        <form @change="onFileSelected">
          <input id="img-select" type="file" style="display: none">
          <label for="img-select">
            <div class="mdi mdi-file-image-plus pa-2" id="img-select-btn"> Image select </div>
          </label>
        </form>
      </div>
    </mq-layout>

    <!-- Submit 버튼 -->
    <div class="mdi mdi-file-upload-outline pa-2" id="submit-btn">
      <input type="submit" value=" Submit" @click="onUpload">
    </div>

    <!-- OCR 결과 출력 -->
    <mq-layout :mq="['lg']">
      <h1 class="mt-6">Result</h1>
      <p style="font-size: 1.3em">Result will come out soon below.</p>
    </mq-layout>
    <mq-layout :mq="['sm', 'md']">
      <h1 class="mt-6 pl-3">Result</h1>
      <p class="pl-3" style="font-size: 1.3em">Result will come out soon below.</p>
    </mq-layout>

    <!-- 처리결과 이미지 -->
    <div class="images">
      <div v-for="(imageurl, index) in images" :key="index" class="image">
        <img :src=imageurl alt="imageOCR"/>
      </div>
    </div>

    <!-- 처리결과 텍스트 -->
    <div class="ocrtext">
      <div v-for="(text, index2) in ocrtext" :key="index2" class="resulttext">
        <p>{{ text }}</p><br>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios';
import PictureInput from 'vue-picture-input';

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

  },
  methods: {
    onFileSelected(event) {
      this.selectedFile = event.target.files[0]
    },
    onUpload() {
      var fd = new FormData();
      fd.append('file', this.selectedFile)
      axios.post('http://localhost:3000/upload', fd)
        .then(this.test());
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
    },
    test() {
      this.timerfunc = setInterval(() => {
        this.$http.get('/api/upload')
          .then((res) => {
            this.ocrtext = res.data.test;
            this.images = res.data.test2;
            if (this.images[0] != null) {
              clearInterval(this.timerfunc);
              if (this.ocrtext[0] == null) {
                this.ocrtext[0] = "No Text";
              }
            }
          })
          .catch((err) => {
            console.error(err);
          });
      }, 3000);
    }
  }
}

</script>

<style>
h1 {
  color: cornflowerblue;
}
ul {
  list-style: none;
}

input[type="file"] {
  cursor: pointer;
}

/* 입력 파트 */
#img-container-pc {
  border: 3px solid cornflowerblue;
  text-align: center;
}
#img-container-mobile, #submit-btn {
  border: 3px solid cornflowerblue;
  border-radius: 4px;
  text-align: center;
  width: 90%;
  height: 46.5px;
  margin: 0 auto;
}
#img-select-btn, #submit-btn {
  font-size: 20px;
}
#submit-btn:hover, #submit-btn:active {
  background: lightgray;
}

/* 출력 파트 */
.image, .resulttext {
  float: left;
  border: 3px solid cornflowerblue;
  padding: 10px;
  margin-top: 10px;
  width: 100%;
}
</style>
