<template>
  <div id="app">
    <div class="header">
      <home-view msg="기본 컴포넌트: HomeView"></home-view>
    </div>
    <router-view/>
    <div class="footer">
      <about-view></about-view>
    </div>
  </div>
</template>
<script>
  import HomeView from './components/HomeView.vue'
  import AboutView from './components/AboutView.vue'
  export default {
    components: {
      HomeView,
      AboutView,
    }
  }
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

div {
  padding: 30px;
}

div a {
  font-weight: bold;
  color: #2c3e50;
}

div a.aboutview-exact-active {
  color: #42b983;
}
</style>
