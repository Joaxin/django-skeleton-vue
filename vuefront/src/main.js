// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueRouter from 'vue-router'
import ElementUI from 'element-ui'
import VueResource  from 'vue-resource'
import routes from './router'
import store from './store/index'

import 'element-ui/lib/theme-chalk/display.css'
import './assets/css/main.css'

Vue.config.productionTip = false

Vue.use(VueRouter)
Vue.use(ElementUI)
Vue.use(VueResource)

const router = new VueRouter({
  //
  mode: 'history',
  routes: routes
})

/* eslint-disable no-new */
new Vue({
  router,
  store
}).$mount('#app')

/* eslint-disable no-new */
// new Vue({
//   el: '#app',
//   router,
//   components: { App },
//   template: '<App/>'
// })
