<template>
    <div>
    <el-row :gutter="20">
        <el-col :xs="8" :sm="6" :md="6" :lg="4" :xl="4" v-for="link in linkList" :key="link.string">
           <!-- Avoid using non-primitive value as key, use string/number value instead. -->
            <a :href="link.url" target="_blank">
                <img :src="link.icon" :alt="link.title" />
                <span>{{ link.title }}</span>
            </a>
        </el-col>
    </el-row>
    <!-- <el-row display="margin-top:10px">
        <el-input v-model="input" placeholder="URL" style="display:inline-table; width: 30%; float:left"></el-input>
        <el-button type="primary" @click="addBook()" style="float:left; margin: 2px;">ADD</el-button>
    </el-row> -->
    <el-row>
        <el-table :data="mylinkList" style="width: 100%" border>
          <!-- <el-table-column prop="id" label="id" min-width="100">
            <template slot-scope="scope"> {{ scope.row.id }} </template>
          </el-table-column>
          <el-table-column prop="ico" label="icon" min-width="100">
            <template slot-scope="scope"> {{ scope.row.ico}} </template>
          </el-table-column>
          <el-table-column prop="title" label="title" min-width="100">
            <template slot-scope="scope"> {{ scope.row.title }} </template>
          </el-table-column>
          <el-table-column prop="url" label="url" min-width="100">
            <template slot-scope="scope"> {{ scope.row.url }} </template>
          </el-table-column>
            <el-table-column prop="category" label="category" min-width="100">
            <template slot-scope="scope"> {{ scope.row.category}} </template>
          </el-table-column>
        <el-table-column prop="tags" label="tags" min-width="100">
            <template slot-scope="scope"> {{ scope.row.tags }} </template>
          </el-table-column> -->
        </el-table>
    </el-row>
    </div>
</template>

<script>
export default {
    data() {
        return {
            linkList: [],
            mylinkList: [],
            // category: "common"
        };
    },
    created() {
        var _link_list = this.$store.getters.baselinks;
        this.linkList = _link_list;
    },
    mounted: function () {
    this.showLinks()
  },
    methods: {
    // addBook () {
    //     http://127.0.0.1:8000/api/favorites/
    //   this.$http.get('http://127.0.0.1:8000/api/add_book?book_name=' + this.input)
    //     .then((response) => {
    //       var res = JSON.parse(response.bodyText)
    //       if (res.error_num === 0) {
    //         this.showBooks()
    //       } else {
    //         this.$message.error('新增书籍失败，请重试')
    //         console.log(res['msg'])
    //       }
    //     })
    // },
    showLinks () {
      this.$http.get('http://127.0.0.1:8000/api/favorites/?format=json').then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          this.mylinkList = res
        //   if (res.error_num === 0) {
        //     this.mylinkList = res
        //   } else {
        //     this.$message.error('Loading failed')
        //     console.log(res['msg'])
        //   }
        }, function (response) {
                  alert("error ");
              // error callback
          })
    }
  }
};
</script>

<style slot-scope>
a {
    display: block;
    padding: 0.5rem 0 0.5rem 1rem;
    margin-bottom: 1rem;
    color: #444d58;
}
a:-webkit-any-link {
    color: none;
    cursor: pointer;
    text-decoration: none;
}
a:hover {
    box-shadow: 0 2px 6px rgba(92, 88, 88, 0.175);
}
a,
a:focus,
a:hover {
    text-decoration: none;
}
img {
    width: 1.2rem;
    margin: 0 0.2rem -0.1rem 0;
}
</style>