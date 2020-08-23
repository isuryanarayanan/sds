var FakeUserDatabase = [
  {
    email: "sukumon",
    password: "sukumon123",
    mode: 1,
  },
  {
    email: "sukumon1",
    password: "sukumon1123",
    mode: 2,
  },
  {
    email: "sukumon2",
    password: "sukumon2123",
    mode: 3,
  },
];
function generateNewTokenForFakeUser() {
  return "newTokenForFakeUser";
}
export default {
  namespaced: true,
  state: {
    token: localStorage.getItem("TOKEN"),
    authenticated: false,
  },
  getters: {
    get_authenticated: function(state) {
      return state.authenticated;
    },
    get_mode: function(state) {
      return state.authenticated;
    },
    get_token: function(state) {
      return state.token;
    },
  },
  mutations: {
    toggle_authenticated: function(state) {
      state.authenticated = !state.authenticated;
    },
    set_authenticated: function(state, st) {
      state.authenticated = st;
    },
    set_token: function(state, token) {
      state.token = token;
      localStorage.setItem("TOKEN", token);
    },
  },
  actions: {
    GET_JWT_TOKEN: function({ rootGetters }, PAYLOAD) {
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

      return promise;
    },

    toggle_authenticated: function(commit) {
      commit("toggle_authenticated");
    },
    get_token: function({ commit }, cred) {
      // Fake user database
      FakeUserDatabase.forEach((user) => {
        if (user.email == cred.email && user.password == cred.password) {
          commit("set_token", generateNewTokenForFakeUser());
          commit("toggle_authenticated");
        }
      });
    },
  },
};
