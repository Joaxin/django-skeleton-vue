import Vue from 'vue'
import Vuex from 'vuex'

import mutations from './mutations'
import Data from '../config/utils'

Vue.use(Vuex)

const state = {
  searchList: Data.searchList,
  linkList: Data.linkList
}

const getters = {
  searchTypes (state) {
    return Object.keys(state.searchList)
  },
  baselinks (state) {
    var _list = []
    var _dic = state.linkList
    for (var key in _dic) {
      var eachList = _dic[key].slice(0, 6)
      _list = _list.concat(eachList)
    }
    return _list
  }
}

export default new Vuex.Store({
  state,
  getters,
  mutations
})
