import Vue from 'vue'
import App from './App.vue'
import Router from 'vue-router'
import ElementUI from 'element-ui'
import VueResource  from 'vue-resource'
import routes from './router/index'
import store from './store/index'

import 'element-ui/lib/theme-chalk/display.css'
import './assets/css/main.css'

Vue.config.productionTip = false

Vue.use(Router)
Vue.use(ElementUI)
Vue.use(VueResource)

const router = new Router({
  //
  mode: 'history',
  routes: routes
})

/* eslint-disable no-new */
new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
