import Vue from "vue";
import Vuex from "vuex";
import messageService from "@/services/messageService";

Vue.use(Vuex);

export default new Vuex.Store({
  namespaced: true,
  state: {
    messages: [],
    category: [],
  },
  getters: {
    messages: state => {
      return state.messages;
    },
    category: state => {
      return state.category;
    },
  },
  mutations: {
    setMessages(state, messages) {
      state.messages = messages;
    },
    addMessage(state, message) {
      state.messages.push(message);
    },
    patchMessage(state, msgId, messages) {
      state.messages = state.messages.splice(msgId, 1, messages);
      state.messages = messages;
    },
    deleteMessage(state, msgId) {
      state.messages = state.messages.filter(obj => obj.id !== msgId);
    },
    setCategory(state, category) {
      state.category = category;
    },

  },
  actions: {
    getMessages({ commit }) {
      messageService.fetchMessages().then(messages => {
        commit("setMessages", messages);
      });
    },
    addMessage({ commit }, message) {
      messageService.postMessage(message).then(() => {
        commit("addMessage", message);
      });
    },
    patchMessage({ commit }, msgId, message) {
      messageService.patchMessage(msgId, message);
      commit("patchMessage", msgId, message);
    },
    deleteMessage({ commit }, msgId) {
      messageService.deleteMessage(msgId);
      commit("deleteMessage", msgId);
    },
    getCategory({ commit }) {
      messageService.fetchCategory().then(category => {
        commit("setCategory", category);
      });
    },
  }
});
