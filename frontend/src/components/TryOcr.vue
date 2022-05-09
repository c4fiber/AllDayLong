<template>
  <div class="tryocr">
    <h1>OCR 시연 페이지</h1>

    <div id="ocrocr">
      <v-container>
        <div class="printImage ma-5 pa-1">
          입력된 이미지 출력 창
        </div>
        <div class="inputImage ma-5 pa-1">
          이미지 입력 창
          Drag & Drop Possible
        </div>
        <div class="printText ma-5 pa-1">
          OCR 결과 출력 창
        </div>
      </v-container>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TryOcr',
  props: {
    msg: String
  }
}
</script>

<style scoped>
  #ocrocr {
    border: 1px solid gray;
  }
  .printImage, .inputImage, .printText {
    border: 3px solid green;
  }
</style>
