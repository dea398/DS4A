import App from "@/App.vue";
import BootstrapVue from "bootstrap-vue";
import router from "@/router";
import Vue from "vue";
import Carousel3d from "vue-carousel-3d";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.min.css";
import vuetify from "./plugins/vuetify";
import VueResource from "vue-resource";
import "vue-material/dist/vue-material.min.css";
import "vue-material/dist/theme/default.css";
import VueLodash from "vue-lodash";

import "@babel/polyfill";

Vue.use(BootstrapVue);
Vue.use(Carousel3d);
Vue.use(vuetify);
Vue.use(VueResource);
Vue.use(VueLodash);

Vue.config.productionTip = false;
Vue.http.options.crossOrigin = true;

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount("#app");
