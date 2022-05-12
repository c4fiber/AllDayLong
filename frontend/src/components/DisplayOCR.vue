<template>
<div>
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
</template>

<script>
export default {
    data() {
        return {
            ocrtext: [],
            images:[],
        };
    },
    created() {
        this.$http.get('/api/upload')
        .then((res) => {
            this.ocrtext = res.data.test;
            this.images=res.data.test2;
        })
        .catch((err) => {
            console.error(err);
        });
    }

}   
</script>

<style>
    .user {
        float: left;
        border: 2px solid black;
        padding: 15px;
        margin: 20px;
    }
    .image{
        float: left;
        border: 2px solid black;
        padding: 15px;
        margin: 20px;
    }

</style>