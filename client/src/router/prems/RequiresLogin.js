import store from "../store/index.js";

function RequiresLogin(record) {
  if (record.hasOwnProperty("requiresLogin")) {
    if (
      record.meta.requiresLogin &&
      store.getters["user/get_authenticated"] == false
    ) {
      console.log("requires login");
      next("/get-started");
    } else {
      next();
    }
  }
}
export default RequiresLogin();
