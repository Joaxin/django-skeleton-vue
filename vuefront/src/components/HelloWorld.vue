<template>
<el-row type="flex" class="row-bg" justify="center">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
    <el-submenu index="1">
      <template slot="title">Installed CLI Plugins</template>
<el-menu-item index="2-1">
    <el-link href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel" target="_blank" rel="noopener norefferrer" >babel</el-link></el-menu-item>
<el-menu-item index="2-2">
    <el-link href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint" target="_blank" rel="noopener norefferrer" >eslint</el-link>
</el-menu-item>
</el-submenu>

<el-submenu index="2">
    <template slot="title">Essential Links</template>
    <el-menu-item index="2-1">
      <el-link href="https://vuejs.org" target="_blank" rel="noopener norefferrer" >Core Docs</el-link></el-menu-item>
    <el-menu-item index="2-2">
      <el-link href="https://forum.vuejs.org" target="_blank" rel="noopener norefferrer" >Forum</el-link></el-menu-item>
    <el-menu-item index="2-3">
      <el-link href="https://chat.vuejs.org" target="_blank" rel="noopener norefferrer" >
      Community Chat</el-link>
      </el-menu-item>
    <el-menu-item index="2-4" disabled>
      <el-link href="https://twitter.com/vuejs" target="_blank" rel="noopener norefferrer" >Twitter</el-link></el-menu-item>
    <el-menu-item index="2-5">
      <el-link href="https://news.vuejs.org" target="_blank" rel="noopener norefferrer" >News</el-link>
    </el-menu-item>
</el-submenu>

<el-submenu index="3">
    <template slot="title">Ecosystem</template>
    <el-menu-item index="3-1">
        <el-link href="https://router.vuejs.org" target="_blank" rel="noopener norefferrer" >vue-router</el-link></el-menu-item>
      <el-menu-item index="3-2"> 
        <el-link href="https://vuex.vuejs.org" target="_blank" rel="noopener norefferrer" >vuex</el-link>
    </el-menu-item>
    <el-menu-item index="3-3">
        <el-link href="https://github.com/vuejs/vue-devtools#vue-devtools" target="_blank" rel="noopener norefferrer" >vue-devtools</el-link>
    </el-menu-item>
          <el-menu-item index="3-4"> 
               <el-link href="https://vue-loader.vuejs.org" target="_blank" rel="noopener norefferrer" 
          >vue-loader</el-link>
    </el-menu-item>
    <el-menu-item index="3-5">
        <el-link href="https://github.com/vuejs/awesome-vue" target="_blank" rel="noopener norefferrer" >awesome-vue</el-link>
  </el-menu-item>
  </el-submenu>
  <el-menu-item index="4"><el-link href="/about" rel="noopener norefferrer" >About</el-link></el-menu-item>
  </el-menu>
</el-row>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
      return {
        activeIndex: '4',
      };
    },
  methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      },
    },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
</style>
