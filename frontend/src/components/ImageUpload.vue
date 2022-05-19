
<template>
  <div>
    <h2>이미지 업로드 구현</h2>
    <br>
    <hr>
    <br>
    <form @change="onFileSelected">
        <input type="file" name="file" id="input-files">
        <label for="file" >Choose file</label>
        <input type="submit" value="Submit"  @click="onUpload">
    </form> 
     <div class="ocrtext">
        <div v-for="(text, index) in ocrtext" :key="index" class="user">
           
            <p>{{ text }} </p><br>
         </div>
    </div>
    <br>
    <div class="images">
      <div v-for="(imageurl, index2) in images" :key="index2" class="image">
        <img :src=imageurl alt="imageOCR"/>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default{
  name:"ImageUpload",
  data(){
    return{
        timerfunc:null,
        ocrtext: [],
        images:[],
    };
  },   
  created(){
    this.timerfunc=setInterval(() =>{ 
        this.$http.get('/api/upload')
        .then((res) => {
        this.ocrtext = res.data.test;
        this.images=res.data.test2;
        if(this.ocrtext[0]!=null){
            clearInterval(this.timerfunc);
        }
        })
        .catch((err) => {
        console.error(err);
        });},1000);
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
            console.log(res);
            })
        this.timerfunc=setInterval(() =>{ 
        this.$http.get('/api/upload')
        .then((res) => {
        this.ocrtext = res.data.test;
        this.images=res.data.test2;
        
        })
        .catch((err) => {
        console.error(err);
        });},1000);
        }
    }
};

</script>

<style>
    button{
        background-color:yellow;
    }
    .user {
        float: left;
        border: 2px solid black;
        padding: 15px;
        margin: 20px;
    }
</style>

