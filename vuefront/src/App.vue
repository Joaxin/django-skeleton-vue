

<template>

  <div id="app">
    <el-row type="flex" class="row-bg" justify="center">
    <el-tabs v-model="activeName" router>
      <el-tab-pane label="Home" name="first"><router-link to="/">1</router-link></el-tab-pane>
      <el-tab-pane label="About" name="second" @click="$router.push('about')"></el-tab-pane>
    </el-tabs>
    </el-row>
    <router-view />
  </div>

</template>

<script>
  export default {
    data() {
      return {
        activeName: 'first'
      };
    },
    methods: {
      handleClick(tab, event) {
        console.log(tab, event);
      }
    }
  };
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
