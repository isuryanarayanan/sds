/* eslint-disable */
import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import store from "../store/index.js";
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },

  {
    path: "/get-started",
    name: "GetStarted",

    component: () => import("../views/GetStarted.vue"),
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: () => import("../views/Dashboard.vue"),
    meta: {
      requiresAuth: true,
    },
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

function runLoad() {
  let locallyStoredAccessToken = localStorage.getItem("ACCTOKEN");
  let locallyStoredRefreshToken = localStorage.getItem("REFTOKEN");
  let TokenVerification = store.dispatch(
    "user/VALIDATE_TOKEN",
    locallyStoredAccessToken
  );

  TokenVerification.then((data) => {
    if (data.status == 200) {
      store.commit("user/set_authenticated", true);
    } else {
      let TokenRefresh = store.dispatch("user/REFRESH_TOKEN", {
        ACC: locallyStoredAccessToken,
        REF: locallyStoredRefreshToken,
      });
      TokenRefresh.then((refresh) => {
        if (refresh.status == 200) {
          console.log("refresh succesfull");
        }
      });
      store.commit("user/set_authenticated", false);
    }
  });
}

router.beforeEach((to, from, next) => {
  runLoad();
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (store.getters["user/get_authenticated"] != false) {
      next();
      return;
    }
    next("/get-started");
  } else {
    next();
  }
});
export default router;
