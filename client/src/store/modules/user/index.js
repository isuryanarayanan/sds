export default {
  namespaced: true,
  state: {
    accessToken: localStorage.getItem("ACCTOKEN"),
    refreshToken: localStorage.getItem("REFTOKEN"),
    authenticated: false,
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
  },
  mutations: {
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
    GET_JWT_TOKEN: function({ rootGetters, commit }, PAYLOAD) {
      let xhr = new XMLHttpRequest();
      let promise = new Promise((resolve, reject) => {
        xhr.open(
          "POST",
          rootGetters.endpoints("BASE") + rootGetters.endpoints("GET_TOKEN")
        );
        xhr.setRequestHeader("Content-Type", "Application/json");
        xhr.onload = () => {
          resolve(xhr);
        };
        xhr.onerror = () => {
          reject(xhr);
        };
        xhr.send(JSON.stringify(PAYLOAD));
      });
      promise.then((data) => {
        commit("set_accessToken", JSON.parse(data.response).access);
        commit("set_refreshToken", JSON.parse(data.response).refresh);
      });
      return promise;
    },
    VALIDATE_TOKEN: function({ rootGetters, getters }) {
      let xhr = new XMLHttpRequest();
      let promise = new Promise((resolve, reject) => {
        xhr.open(
          "GET",
          rootGetters.endpoints("BASE") + rootGetters.endpoints("VAL_TOKEN")
        );
        xhr.setRequestHeader("Content-Type", "Application/json");
        xhr.setRequestHeader(
          "Authorization",
          "Bearer " + getters["get_accessToken"]
        );
        xhr.onload = () => {
          resolve(xhr);
        };
        xhr.onerror = () => {
          reject(xhr);
        };
        xhr.send();
      });
      return promise;
    },
    REFRESH_TOKEN: function({ rootGetters, getters }) {
      let xhr = new XMLHttpRequest();
      let promise = new Promise((resolve, reject) => {
        xhr.open(
          "GET",
          rootGetters.endpoints("BASE") + rootGetters.endpoints("REF _TOKEN")
        );
        xhr.setRequestHeader("Content-Type", "Application/json");
        xhr.setRequestHeader(
          "Authorization",
          "Bearer " + getters["get_accessToken"]
        );
        xhr.onload = () => {
          resolve(xhr);
        };
        xhr.onerror = () => {
          reject(xhr);
        };
        xhr.send();
      });
      return promise;
    },
  },
};
