import App from "@/App.vue";
import BootstrapVue from "bootstrap-vue";
import router from "@/router";
import Vue from "vue";
import Carousel3d from "vue-carousel-3d";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.min.css";


Vue.config.productionTip = false;
Vue.use(BootstrapVue);
Vue.use(Carousel3d);

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
