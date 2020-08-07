import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Customer from "../views/Customer.vue";
import Vendor from "../views/Vendor.vue";
import Administrator from "../views/Administrator.vue";

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
    path: "/about",
    name: "About",
    component: () => import("../views/About.vue"),
  },
  {
    path: "/c",
    name: "CustomerView",
    component: Customer,
  },
  {
    path: "/v",
    name: "VendorView",
    component: Vendor,
  },
  {
    path: "/administrator",
    name: "AdministratorView",
    component: Administrator,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
