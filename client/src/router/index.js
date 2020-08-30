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
    beforeEnter: function(to, from, next) {
      if (store.getters["user/get_authenticated"]) {
        next({ name: "Dashboard" });
      } else {
        next();
      }
    },
  },

  {
    path: "/get-started",
    name: "GetStarted",
    component: () => import("../views/GetStarted.vue"),
    beforeEnter: function(to, from, next) {
      if (store.getters["user/get_authenticated"]) {
        next({ name: "Dashboard" });
      } else {
        next();
      }
    },
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: () => import("../views/Dashboard.vue"),
    beforeEnter: function(to, from, next) {
      if (store.getters["user/get_authenticated"]) {
        next();
      } else {
        next({ name: "GetStarted" });
      }
    },
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

function runLoad() {
  let promise = new Promise((resolve, reject) => {
    store.dispatch("user/VALIDATE_TOKEN").then((data) => {
      if (data.status == 200) {
        store.commit("user/set_authenticated", true);
        resolve();
      } else {
        store.dispatch("user/REFRESH_TOKEN").then((refresh) => {
          if (refresh.status == 200) {
            store.commit(
              "user/set_accessToken",
              JSON.parse(refresh.response).access
            );
            store.commit("user/set_authenticated", true);
            resolve();
          } else {
            store.commit("user/set_authenticated", false);
            resolve();
          }
        });
      }
    });
  });
  return promise;
}

router.beforeEach((to, from, next) => {
  runLoad().then(() => {
    next();
  });
});
export default router;
