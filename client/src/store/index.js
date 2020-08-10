import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    authenticated: false,
  },
  getters: {
    get_authenticated: function({ state }) {
      return state.authenticated;
    },
  },
  mutations: {
    toggle_authenticated: function({ state }) {
      state.authenticated = !state.authenticated;
    },
  },
  actions: {
    set_authentication_status: function({ commit }) {
      commit("toggle_authenticated");
    },
  },
  modules: {},
});
