/* eslint-disable */
import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import PermissionEngine from "../router/engine.js";
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
    meta: {
      requiresLogin: true,
    },
    children: [
      {
        path: "/c",
        name: "CustomerDashboard",
        component: () => import("../views/Dashboard.vue"),
        meta: {
          requiresLogin: true,
          requiresMode: {
            require: true,
            mode: 1,
          },
        },
      },
    ],
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
