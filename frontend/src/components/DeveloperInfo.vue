<template>
  <div v-if="developer">
    <h1>개발자 상세 정보</h1>
    <p>아이디: {{ developer.id }} </p>
    <p>비밀번호: {{ developer.password }} </p>
    <p>이름: {{ developer.name }} </p>
    <p>역할: {{ developer.role }} </p>
    <p>실시간 적용 확인 호잇</p>
  </div>
  <div v-else>
    <h1> 존재하지 않는 멤버입니다. </h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      developer: null
    }
  },
  created() {
    var id = this.$route.params.id

    this.$http.get(`/api/developers/${id}`)
      .then((res) => {
        const developer = res.data.developer;
        if (developer) this.developer = developer;
      })
      .catch((err) => {
        console.error(err);
      });
  }
}
</script>

<style>
</style>
