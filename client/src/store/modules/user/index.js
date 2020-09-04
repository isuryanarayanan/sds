import GET_JWT_TOKEN from "../user/actions/GET_JWT_TOKEN.js";
import VALIDATE_TOKEN from "../user/actions/VALIDATE_TOKEN.js";
import REFRESH_TOKEN from "../user/actions/REFRESH_TOKEN.js";
import REGISTER_USER from "../user/actions/REGISTER_USER.js";
import GET_USER from "../user/actions/GET_USER.js";
export default {
  namespaced: true,
  state: {
    accessToken: localStorage.getItem("ACCTOKEN"),
    refreshToken: localStorage.getItem("REFTOKEN"),
    authenticated: false,
    user: {
      loaded: false,
      username: null,
      email: null,
    },
  },
  getters: {
    get_authenticated: function(state) {
      return state.authenticated;
    },
    get_accessToken: function(state) {
      return state.accessToken;
    },
    get_refreshToken: function(state) {
      return state.refreshToken;
    },
    get_if_user_loaded: function(state) {
      return state.user.loaded;
    },
  },
  mutations: {
    set_user_if_loaded: function(state, st) {
      state.user.loaded = st;
    },
    set_authenticated: function(state, st) {
      state.authenticated = st;
    },
    set_accessToken: function(state, token) {
      state.accessToken = token;
      localStorage.setItem("ACCTOKEN", token);
    },
    set_refreshToken: function(state, token) {
      state.refreshToken = token;
      localStorage.setItem("REFTOKEN", token);
    },
  },
  actions: {
    GET_JWT_TOKEN,
    VALIDATE_TOKEN,
    REFRESH_TOKEN,
    REGISTER_USER,
    GET_USER,
  },
};
