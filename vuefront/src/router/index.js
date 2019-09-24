/* eslint-disable */ 

// import Vue from 'vue'
// import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'

// Vue.use(Router)

// export default new Router({
//   routes: [
//     {
//       path: '/',
//       name: 'HelloWorld',
//       component: HelloWorld
//     }
//   ]
// })

import App from '@/App'

// 实现按需加载
const home = r => require.ensure([], () => r(require('@/page/home')), 'home')

// 定义路由
export default [{
    path: '/',
    component: App,
    children: [
        {
            path: '',
            component: home
        }
    ]
}]
