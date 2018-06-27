import Vue from 'vue';
import Vuex from 'vuex';

import nodesGraphState from './modules/nodesGraphState/store';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    nodesGraphState,
  }
});
