import Vue from 'vue'
import App from './App.vue'

export const bus = new Vue();

import store from './store/store';

new Vue({
  el: '#app',
  store,
  render: h => h(App)
});
