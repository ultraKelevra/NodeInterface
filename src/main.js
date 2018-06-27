import Vue from 'vue';
import App from './App.vue';
import VueResource from 'vue-resource';
import store from './store/store';

Vue.use(VueResource);
Vue.http.options.root = 'http://127.0.0.1:5000/';

export const bus = new Vue();

new Vue({
  el: '#app',
  store,
  render: h => h(App)
});
