import store from "../../store/index.js";

export default (arg, record) => {
  if (
    record.meta.requiresMode &&
    store.getters["user/get_mode"] == record.meta.requiresMode
  ) {
    console.log("Action protected by customer");
    arg.next("/get-started");
  } else {
    arg.next();
  }
};
