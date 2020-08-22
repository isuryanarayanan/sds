import Vue from "vue";
import Vuex from "vuex";
import user from "./modules/user/index.js";
Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  getters: {},
  mutations: {},
  actions: {
    load: function({ commit }) {
      // locallyStoredToken = localStorage.getItem("TOKEN");
      let valid = true;
      if (valid) {
        commit("user/set_authenticated", true);
      } else {
        commit("user/set_authenticated", false);
      }
    },
  },
  modules: { user },
});
