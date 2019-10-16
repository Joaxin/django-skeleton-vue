import Vue from "vue";
import Vuex from "vuex";
import messageService from "@/services/messageService";

Vue.use(Vuex);

export default new Vuex.Store({
  namespaced: true,
  state: {
    messages: [],
    category: [],
    form: {
      id: 0,
      content: "",
      category: '',
      tags: ['Hello World'],
      inputVisible: false,
      inputValue: '',
    },
  },
  getters: {
    messages: state => {
      return state.messages;
    },
    category: state => {
      return state.category;
    },
    form: state => {
      return state.form;
    }
  },
  mutations: {
    setMessages(state, messages) {
      state.messages = messages;
    },
    addMessage(state, message) {
      state.messages.push(message);
    },
    getMessage(state, message) {
      state.form.id = message.id
      state.form.content = message.content
      state.form.category = message.category
      state.form.tags = message.tags
    },
    putMessage(state, msgId, message) {
      let msgs= state.messages.splice(msgId, 1, message);
      state.messages = msgs;
    },
    patchMessage(state, msgId, message) {
      let msgs= state.messages.splice(msgId, 1, message);
      state.messages = msgs;
    },
    deleteMessage(state, msgId) {
      state.messages = state.messages.filter(obj => obj.id !== msgId);
    },
    setCategory(state, category) {
      state.category = category;
    }
  },
  actions: {
    getMessages({ commit }) {
      messageService.fetchMessages().then(messages => {
        commit("setMessages", messages);
      });
    },
    getMessage({ commit }, msgId) {
      messageService.getMessage(msgId).then(message => {
        commit("getMessage", message);
      });
    },
    addMessage({ commit }, message) {
      messageService.postMessage(message).then(() => {
        commit("addMessage", message);
      });
    },
    putMessage({ commit }, message) {
      messageService.putMessage(message.id, message);
      commit("putMessage", message.id, message);
    },
    patchMessage({ commit }, message) {
      messageService.patchMessage(message.id, message);
      commit("patchMessage", message.id, message);
    },
    deleteMessage({ commit }, msgId) {
      messageService.deleteMessage(msgId);
      commit("deleteMessage", msgId);
    },
    getCategory({ commit }) {
      messageService.fetchCategory().then(category => {
        commit("setCategory", category);
      });
    }
  }
});
