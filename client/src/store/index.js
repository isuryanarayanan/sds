import Vue from "vue";
import Vuex from "vuex";
import user from "./modules/user/index.js";
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    endpoints: {
      /* base url for the backend server */
      BASE: "http://127.0.0.1:8000/",
      /* authentication endpoints */
      GET_TOKEN: "accounts/api/token/", // endpoint to get the token
      REF_TOKEN: "accounts/api/token/refresh/", // endpoint to refresh the active access token
      VAL_TOKEN: "accounts/api/token/validate/", // endpoint to validate the active access token
      /* authorization endpoints */
      GET_USER: "accounts/api/authorization/user/", //endpoint to get user details
    },
  },
  getters: {
    endpoints: (state) => {
      return (key) => {
        return state.endpoints[key];
      };
    },
  },
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
