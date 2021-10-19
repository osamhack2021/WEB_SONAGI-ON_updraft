import Vue from 'vue';
import axios from 'axios';
import App from './App.vue';
import router from './router';
import vuetify from './plugins/vuetify';
import store from './store';
import VueSimpleAlert from "vue-simple-alert";

Vue.use(VueSimpleAlert); // https://vuejsexamples.com/simple-alert-for-vue-js/

Vue.config.productionTip = false;
Vue.prototype.axios = axios;
new Vue({
  router,
  vuetify,
  store,
  render: h => h(App),
}).$mount('#app')