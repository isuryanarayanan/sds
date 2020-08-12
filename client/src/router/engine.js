import RequiresLogin from "./prems/RequiresLogin.js";

export default (to, from, next) => {
  var record = to.matched.some((rec) => {
    return rec;
  });
  RequiresLogin(record);
  //   RequiresMode(record);
};
