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


</div>
</template>
<script>

    import axios from 'axios';

export default{
    name:"ImageUpload",
    data(){
        return{
            selectedFile:null
        };
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
        }
        
    }
};

  
    



</script>

<style>
    button{
        background-color:yellow;
    }

</style>

