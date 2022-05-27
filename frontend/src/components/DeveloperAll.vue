<template>
  <div class="developers">
    <div class="team_name">
      <h1>Team AllDayLong</h1>
      <p class="team_name_description">
        : 밤낮 가리지 않고 하루종일 작업하는 AllDayLong 팀을 소개합니다.
      </p>
    </div>
    <div v-for="(developer, index) in developers" :key="index" class="developer">
      <h2>Developer {{ index+1 }}</h2>
      <p>아이디 &nbsp; : &nbsp; {{ developer.id }} </p>
      <p>이 &nbsp;&nbsp; 름 &nbsp; : &nbsp; {{ developer.name }} </p>
      <p>역 &nbsp;&nbsp; 할 &nbsp; : &nbsp; {{ developer.role }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      developers: []
    };
  },
  created() {
    this.$http.get('/api/developers')
      .then((res) => {
        this.developers = res.data.developers;
      })
      .catch((err) => {
        console.error(err);
      });
  }
}
</script>

<style>
.team_name {
  margin: 20px 0px 30px 0px;
}

.developer {
  border: 2px solid black;
  padding: 15px;
  margin: 20px;
}

.team_name_description {
  font-size: 1.4em;
  margin-top: 10px;
  margin-left: 20px;
}

h1, h2 {
  color: cornflowerblue;
  margin-bottom: 10px;
}

p {
  font-size: 1.1em;
  font-weight: bold;
}
</style>
