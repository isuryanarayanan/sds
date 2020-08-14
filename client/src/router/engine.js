import RequiresLogin from "./prems/RequiresLogin.js";
import RequiresMode from "./prems/RequiresMode.js";
export default (arg) => {
  arg.to.matched.some((record) => {
    var perms =
      RequiresLogin(record).satisfied & RequiresMode(record).satisfied;
    if (perms) {
      arg.next();
    } else {
      runPermDirectOfIndex();
    }
  });
};
