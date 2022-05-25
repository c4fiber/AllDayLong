import Vue from 'vue'
import Router from 'vue-router'

// Component List
import HomeView from '@/components/HomeView'
import AboutView from '@/components/AboutView'
import DeveloperAll from '@/components/DeveloperAll'
import DeveloperInfo from '@/components/DeveloperInfo'
import HelloWorld from '@/components/HelloWorld'
import CreateView from '@/components/CreateView'
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
      path: '/developers',
      name: 'Developers',
      component: DeveloperAll
    },
    {
      path: '/developers/:id',
      name: 'DeveloperInfo',
      component: DeveloperInfo
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
