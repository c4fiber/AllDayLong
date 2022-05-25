<template>
  <v-app>
    <!-- 상단 메뉴-->
    <v-app-bar app clipped-left>
      <!-- 메뉴 버튼 -->
      <v-app-bar-nav-icon
        class="d-md-none d-lg-none d-xl-none"
        @click.stop="drawer = !drawer">
      </v-app-bar-nav-icon>

      <!-- 로고 -->
      <a href="/"><img src="@/assets/image/ORCA.png" height="64px"></a>
      <v-spacer />

      <!-- Github -->
      <v-btn text href="https://github.com/c4fiber/AllDayLong">
        <v-icon>mdi-github</v-icon>
      </v-btn>
    </v-app-bar>

    <!-- 왼쪽 메뉴 -->
    <v-navigation-drawer
      app clipped
      v-model="drawer"
      mobile-breakpoint="960"
    >
      <!-- 메뉴 리스트 -->
       <v-list>
         <v-list-item
           v-for="leftmenu in leftmenus"
           :key="leftmenu.title"
           link
           :to="leftmenu.to"
         >
           <v-list-item-icon>
             <v-icon v-text="leftmenu.icon"></v-icon>
            </v-list-item-icon>
           <v-list-item-content>
             <v-list-item-title v-text="leftmenu.title"></v-list-item-title>
           </v-list-item-content>
         </v-list-item>
       </v-list>
    </v-navigation-drawer>

    <!-- 메인 content 위치 -->
    <v-main>
      <v-container>
        <!-- Top 버튼 -->
        <v-btn
          fab dark fixed bottom right
          color="teal"
          @click="$vuetify.goTo(0)"
        >
          <v-icon>mdi-chevron-double-up</v-icon>
        </v-btn>
        <!-- router에 연결된 항목 출력 -->
        <router-view>
        </router-view>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    drawer: null,

    leftmenus: [
      {title: 'Home', icon: 'mdi-home', to: '/'},
      {title: 'Developers', icon: 'mdi-account-multiple', to: '/developers'},
      {title: 'About', icon: 'mdi-help-box', to:'about'},
      {title: 'ORCA\'s Strength' , icon: 'mdi-information', to: '/create'},
      {title: 'Test(여기부턴 보류)', icon: 'mdi-plus-box', to: '/helloworld'},
      {title: 'ImageUpload', icon: 'mdi-image-plus', to: '/upload'},
      {title: 'DisplayOCR', icon: 'mdi-cast-variant', to: '/display'},
    ]
  })
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,400;1,300;1,400&display=swap');
</style>
