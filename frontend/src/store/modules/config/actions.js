export default {
  FORCE_AUTHENTICATE: ({ commit }) => {
    commit("TOGGLE_authenticated");
  },
};
