
<template>
  <div id="app">
      <el-row type="flex" class="row-bg" justify="center">
      <el-menu :default-active="$route.path"  class="el-menu-demo" mode="horizontal" router>
        <el-menu-item index="/">Home</el-menu-item>
        <el-menu-item  index="/about">About</el-menu-item>
      </el-menu>
    </el-row>
    <router-view />
  </div>

</template>

<script>

</script>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

</style>
