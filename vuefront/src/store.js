import Vue from "vue";
import Vuex from "vuex";
import messageService from "@/services/messageService";

Vue.use(Vuex);

export default new Vuex.Store({
  namespaced: true,
  state: {
    messages: []
  },
  getters: {
    messages: state => {
      return state.messages;
    }
  },
  mutations: {
    setMessages(state, messages) {
      state.messages = messages;
    },
    addMessage(state, message) {
      state.messages.push(message);
    },
    deleteMessage(state, msgId) {
      state.messages = state.messages.filter(obj => obj.id !== msgId);
    }
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
    deleteMessage({ commit }, msgId) {
      messageService.deleteMessage(msgId);
      commit("deleteMessage", msgId);
    }
  }
});
