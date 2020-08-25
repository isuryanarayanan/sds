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
  store.dispatch("user/VALIDATE_TOKEN").then((data) => {
    if (data.status == 200) {
      store.commit("user/set_authenticated", true);
    } else {
      store.dispatch("user/REFRESH_TOKEN").then((refresh) => {
        console.log(refresh.response);
        if (refresh.status == 200) {
          store.commit(
            "user/set_accessToken",
            JSON.parse(refresh.response).access
          );
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
