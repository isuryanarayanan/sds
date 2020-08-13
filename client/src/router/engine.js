import RequiresLogin from "./prems/RequiresLogin.js";

export default (arg) => {
  arg.to.matched.some((record) => {
    if ("requiresLogin" in record.meta) {
      RequiresLogin(arg, record);
    }

    arg.next();
  });
};
