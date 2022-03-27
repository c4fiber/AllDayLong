<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <h1 v-if="msg">{{ msg }}</h1>
    <h1 v-else>HomeView 호출</h1>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  props: {
    msg: String
  }
}
</script>
