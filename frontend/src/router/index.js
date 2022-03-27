import Vue from 'vue'
import Router from 'vue-router'

// Component List
import HomeView from '@/components/HomeView'
import AboutView from '@/components/AboutView'
import UserAll from '@/components/UserAll'
import UserInfo from '@/components/UserInfo'
import HelloWorld from '@/components/HelloWorld'


Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'About',
      component: AboutView
    },
    {
      path: '/users',
      name: 'Users',
      component: UserAll
    },
    {
      path: '/users/:id',
      name: 'UserInfo',
      component: UserInfo
    },
    {
      path: '/helloworld',
      name: 'HelloWorld',
      component: HelloWorld
    }

  ]
})