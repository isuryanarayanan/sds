import store from "../../store/index.js";

export default (arg, record) => {
  if (
    record.meta.requiresLogin &&
    store.getters["user/get_authenticated"] == false
  ) {
    arg.next("/get-started");
  } else {
    arg.next();
  }
};
