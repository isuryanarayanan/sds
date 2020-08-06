export default {
  FORCE_AUTHENTICATE_USER: ({ commit }) => {
    commit("TOGGLE_authenticated");
  },
};
