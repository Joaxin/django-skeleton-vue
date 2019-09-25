<template>
<el-row type="flex" class="row-bg" justify="center">
  <el-card class="box-card">
  <div slot="header" class="clearfix">
    <span>{{ msg }}</span>
    <el-button style="float: right; padding: 3px 0" type="text"> <el-link href="https://cli.vuejs.org" target="_blank" rel="noopener"
        >Documentation</el-link></el-button>
  </div>
  <div class="text item">
    For a guide and recipes on how to configure / customize this project,<br />
      check out the
      <el-link href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</el-link>
  </div>
</el-card>
</el-row>
</template>

<script>
export default {
  name: "HelloCard",
  props: {
    msg: String,
  },
};
</script>

<style scoped lang="scss">
  .el-row {
    margin-top: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
</style>