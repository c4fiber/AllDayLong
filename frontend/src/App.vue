<template>
  <v-app>
    <!-- 상단 메뉴-->
    <v-app-bar app clipped-left>
      <v-app-bar-nav-icon
        class="d-md-none d-lg-none d-xl-none"
        @click.stop="drawer = !drawer">
      </v-app-bar-nav-icon>
      <a href="/"><img src="@/assets/image/ORCA.png" height="64px"></a>
      <v-spacer />

      <v-btn text>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
      <v-btn text href="https://github.com/c4fiber/AllDayLong">
        <v-icon>mdi-github</v-icon>
      </v-btn>
<!--      &lt;!&ndash; 반응형 시 띄울 메뉴 icon&ndash;&gt;-->
<!--      <v-menu offset-y>-->
<!--        <template v-slot:activator="{on, attrs}">-->
<!--          <v-btn-->
<!--            text-->
<!--            class=""-->
<!--            v-bind="attrs"-->
<!--            v-on="on"-->
<!--          >-->
<!--            <v-icon>mdi-dots-grid</v-icon>-->
<!--          </v-btn>-->
<!--        </template>-->
<!--      </v-menu>-->

      <!-- 다국어 -->
      <v-menu offset-y>
        <template v-slot:activator="{on, attrs}">
          <v-btn
            text
            class=""
            v-bind="attrs"
            v-on="on"
          >
            <v-icon>mdi-translate</v-icon>
          </v-btn>
        </template>
        <v-list>
          <vlist-item
            v-for="(language, index) in languages"
            :key="index">
            <v-list-item-title v-text="language.title">}</v-list-item-title>
          </vlist-item>
        </v-list>
      </v-menu>
    </v-app-bar>

    <!-- 왼쪽 메뉴 -->
    <v-navigation-drawer
      app clipped
      v-model="drawer"
      mobile-breakpoint="960"
    >
      <!-- 메뉴 리스트 -->
      <v-list>
        <v-list-group
          v-for="leftmenu in leftmenus"
          :key="leftmenu.title"
          v-model="leftmenu.active"
          :prepend-icon="leftmenu.action"
          no-action
        >
          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title v-text="leftmenu.title"></v-list-item-title>
            </v-list-item-content>
          </template>

          <v-list-item
            v-for="leftsubmenu in leftmenu.leftmenus"
            :key="leftsubmenu.title"
            link
            :to="leftsubmenu.to"
          >
            <v-list-item-content>
              <v-list-item-title v-text="leftsubmenu.title"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
      </v-list-group>
      </v-list>
    </v-navigation-drawer>

    <!-- 메인 content 위치 -->
    <v-main>
      <v-container>
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
      {
        action: 'mdi-information',
        leftmenus: [
          {title: 'Introduction', to: '/about'},
          {title: 'Developers', to: '/users'}
        ],
        title: 'About ORCA'
      },
      {
        action: 'mdi-apple',
        leftmenus: [
          {title: 'Create', to: '/create'},
          {title: 'Hello', to: '/helloworld'},
          {title: 'TryOCR', to: '/tryocr'},
          {title: 'ImageUpload', to: '/upload'}
        ],
        title: 'Function1'
      },
      {
        action: 'mdi-ipod',
        leftmenus: [
          {title: 'Create'},
          {title: 'Read'},
          {title: 'Update'},
          {title: 'Delete'}
        ],
        title: 'Function2'
      },
      {
        action: 'mdi-palette',
        leftmenus: [
          {title: 'Create'},
          {title: 'Read'},
          {title: 'Update'},
          {title: 'Delete'}
        ],
        title: 'Function3'
      }
    ],
    languages: [
      {title: 'Korean'},
      {title: 'English'}
    ]
  })
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,400;1,300;1,400&display=swap');
</style>
