<template>
<div class="container">
  <br>
  <br>
 <el-row type="flex" class="row-bg" justify="center">

    <el-col :span="24">
    <el-popover placement="right" title="Tips" width="200" trigger="hover" 
    content="The data below is added/removed from the SQLite Database using Django's ORM and Rest Framework.">
        <el-button slot="reference">Messages on Database</el-button>
    </el-popover> 
    <br>
    <br>
    <el-button type="primary" icon="el-icon-plus" circle  @click="dialogVisible = true"></el-button>

    <el-dialog
    title="Add Messages"
    :visible.sync="dialogVisible"
    width="30%">

    <el-form ref="form" :model="form" label-width="80px">
  <el-form-item label="Category">
      <el-select v-model="form.category" placeholder="category">
      <el-option v-for="(msg, index) in messages" :key="index" v-html="msg.category_name" value="this.value"></el-option>
      </el-select>
  </el-form-item>

  <el-form-item label="Tags">
    <el-tag :key="tag" v-for="tag in form.dynamicTags" closable :disable-transitions="false" @close="handleClose(tag)">
      {{tag}}
    </el-tag>
    <el-input class="input-new-tag" v-if="form.inputVisible" v-model="form.inputValue" ref="saveTagInput" size="small"
      @keyup.enter.native="handleInputConfirm" @blur="handleInputConfirm">
</el-input>
<el-button v-else class="button-new-tag" size="small" @click="showInput"  icon="el-icon-plus" circle ></el-button>

  </el-form-item>

  <el-form-item label="Content">
    <el-input type="textarea" v-model="form.content"></el-input>
  </el-form-item>
</el-form>

    <span slot="footer" class="dialog-footer">
      <el-button type="primary"
      @click="addMessage({ author: 1, content: form.content, category: form.category, tags:form.dynamicTags})" 
      :disabled="!form.content || !form.category">Submit</el-button>
    </span>
  </el-dialog>
    </el-col>
</el-row>
<el-divider></el-divider>
<p v-if="messages.length === 0">No Messages</p>
<el-row :gutter="15">
  <el-col :xs="24" :sm="12" :md="8" :lg="8" v-for="(msg, index) in messages" :key="index">
      <el-card class="box-card" >
          <div slot="header" class="clearfix">
            <el-button style="float: right;" type="submit" @click="deleteMessage(msg.id)" circle><i class="el-icon-delete"></i></el-button>
              
              <el-badge :value="index" class="item">
                <el-button size="small"  v-html="msg.author_name"></el-button>
              </el-badge>
              <br>
              <el-button type="primary"  style="float: left;margin-right:10px;" plain v-html="msg.category_name"></el-button>
              <br>
              <br>
          </div>
          <div class="text item" v-html="msg.content.replace(/\r?\n/g, '<br />')"></div>
          <br>
          <i class="el-icon-time"><time class="time" v-html="msg.created"></time></i><br>
          <i class="el-icon-sort"><time class="time" v-html="msg.updated"></time></i><br>
                       <br>
              <el-tag class="tags"
                v-for="tag in msg.tags"
                :key="tag" type="success">
                {{tag}}
              </el-tag>
      </el-card>
  </el-col>
</el-row>




</div>
</template>

<script>
import { mapState, mapActions } from "vuex"
export default {
  name: "Messages",
  data() {
    return {
      dialogVisible: false,
      form: {
          content: "",
          category: '',
          dynamicTags: ['A', 'B', 'C'],
          inputVisible: false,
          inputValue: ''
        }
    };
  },
  computed: mapState({
    messages: state => state.messages
  }),
  methods: 
  mapActions([
    "addMessage",
    "deleteMessage",
  ]),
  created() {
    this.$store.dispatch("getMessages")
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.box-card{
  margin-top:20px;
  margin-bottom:20px;
}

  .time {
    font-size: 13px;
    color: #999;
  }

  .tags{
    margin-right: 10px;
    margin-bottom: 5px;
  }

  .el-tag + .el-tag {
    margin-left: 10px;
  }
  .button-new-tag {
    margin-left: 10px;
    height: 32px;
    line-height: 30px;
    padding-top: 0;
    padding-bottom: 0;
  }
  .input-new-tag {
    width: 90px;
    margin-left: 10px;
    vertical-align: bottom;
  }
</style>


