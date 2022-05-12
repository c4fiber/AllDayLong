import Vue from 'vue'
import Router from 'vue-router'

// Component List
import HomeView from '@/components/HomeView'
import AboutView from '@/components/AboutView'
import UserAll from '@/components/UserAll'
import UserInfo from '@/components/UserInfo'
import HelloWorld from '@/components/HelloWorld'
import CreateView from '@/components/CreateView'
import TryOcr from '@/components/TryOcr'
import ImageUpload from '@/components/ImageUpload'
import DisplayOCR from '@/components/DisplayOCR'

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
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
      path: '/tryocr',
      name: 'TryOcr',
      component: TryOcr
    },
    {
      path:'/upload',
      name:'UploadImage',
      component: ImageUpload
    },
    {
      path:'/display',
      name:'DisplayOCR',
      component:DisplayOCR
    }
  ]
})
