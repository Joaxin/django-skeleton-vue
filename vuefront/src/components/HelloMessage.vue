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

    <el-dialog title="Add Messages" :visible.sync="dialogVisible" width="30%"  :before-close="handleDataClose">
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="Category">
          <el-select placeholder="category" v-model="form.category" >
          <el-option v-for="(cate, index) in category" :key="index" v-html="cate.name" :value="cate.id" :label="cate.name"></el-option>
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
        @click="addMessage({ author: 1, content: form.content, category: form.category , tags:form.dynamicTags})" 
        :disabled="!form.content || !form.dynamicTags  ">Submit</el-button>
      </span>
  </el-dialog>

  </el-col>
</el-row>
<el-divider></el-divider>
<p v-if="messages.length === 0">No Messages</p>

<el-row :gutter="18">
  <el-col :xs="24" :sm="12" :md="8" :lg="8" v-for="(msg, index) in messages" :key="index">

      <el-card class="box-card" >
          <div slot="header">
              <el-badge :value="index + 1" class="item" style="float: left;margin-right:10px;margin-top:15px;">
                <el-button size="small"  v-html="msg.author_name"></el-button>
              </el-badge>
              <el-button type="primary" size="small"  style="float: left;margin-right:10px;margin-top:15px;margin-left:10px;" plain v-html="msg.category_name"></el-button>

            <el-button style="float: right;margin-top:10px;" type="submit" @click="patchMessage(msg.id, 
            { author: 1, content: 'hshahaha', category: 1 , tags:['ABC']}
            )" circle><i class="el-icon-edit"></i></el-button>
            
            <el-button style="float: right;margin-top:10px;" type="submit" @click="deleteMessage(msg.id)" circle><i class="el-icon-delete"></i></el-button>
              

              <br>
              
              <br>
              <br>
          </div>
          <div class="text item" v-html="msg.content.replace(/\r?\n/g, '<br />')"></div>
          <br>
          <i class="el-icon-time"><time class="time" v-html="msg.created"></time></i><br>
          <i class="el-icon-sort"><time class="time" >{{msg.updated}}</time></i><br>
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
import { mapState } from "vuex"
export default {
  name: "Messages",
  inject: ['reload'],
  data() {
    return {
      dialogVisible: false,
      form: {
          content: "",
          category: '',
          dynamicTags: ['ABC', 'Hello World'],
          inputVisible: false,
          inputValue: ''
        }
    };
  },
  computed: mapState({
    messages: state => state.messages,
    category: state => state.category
  }),
  methods: 
    {
      addMessage(item){
        this.$store.dispatch("addMessage",item)
      },
      patchMessage(pk, item){
        this.$store.dispatch("patchMessage",pk, item)
        this.reload()
      },
      deleteMessage(pk){
        this.$store.dispatch("deleteMessage",pk)
      },
      handleClose(tag) {
        this.form.dynamicTags.splice(this.form.dynamicTags.indexOf(tag), 1);
      },

      showInput() {
        this.form.inputVisible = true;
        this.$nextTick(_ => {
          this.$refs.saveTagInput.$refs.input.focus();
        });
      },

      handleInputConfirm() {
        let inputValue = this.form.inputValue;
        if (inputValue) {
          this.form.dynamicTags.push(inputValue);
        }
        this.form.inputVisible = false;
        this.form.inputValue = '';
      },
      handleDataClose(done) {
        this.reload()
      }
    },
    created() {
    this.$store.dispatch("getMessages"),
    this.$store.dispatch("getCategory")
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


