import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

import config from "./modules/config/index";

export default new Vuex.Store({
  state: {},
  getters: {},
  mutations: {},
  actions: {},
  modules: { config },
});
