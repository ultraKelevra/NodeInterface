import Vue from 'vue';
import Vuex from 'vuex';

import graphState from './modules/graphState';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    graphState,
  }
});
