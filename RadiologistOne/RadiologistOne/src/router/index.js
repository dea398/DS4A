import Vue from "vue";
import VueRouter from "vue-router";

import Description from "@/views/Description.vue";
import Who_We_Are from "@/views/Who_We_Are.vue";
import EDA from "@/views/EDA.vue";
import Demo from "@/views/Demo.vue";
import Demo2 from "@/views/Demo2.vue";
import Contact_Us from "@/views/Contact_Us.vue";
Vue.use(VueRouter);

// TODO Web Template Studio: Add routes for your new pages here.
export default new VueRouter({
  mode: "history",
  routes: [
    { path: "/Contact_Us", component: Contact_Us },
    { path: "/Demo2", component: Demo2 },
    { path: "/Demo", component: Demo },
    { path: "/Who_We_Are", component: Who_We_Are },
    { path: "/Description", component: Description },
    { path: "/EDA", component: EDA},
    { path:"/", redirect: "/Description" }
  ]
});
