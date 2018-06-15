import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
      nodes: [],
      inputs: [],
      outputs: [],
      connections: []
    },
    getters: {
      node(state, id) {
        return state.node.find(elem => id === elem.id);
      },
      inputsOfNode(state, id) {
        return state.node(id).inputs;
      },
      outputsOfNode(state, id) {
        return state.node(id).outputs;
      },
      input({inputs}, id) {
        return inputs.find(input => id === input.id);
      }
    },
    mutations: {
      disconnect(inputId) {
        let input = input(inputId);
        let output = input.connectedOutput;
        input.connected = false;
        input.connectedOutput = null;
        output.connectedInputs.splice(output.connectedInputs.indexOf(input), 1);
      },
      deleteNode(state, id) {
        let node = node(id);
        node.inputs.map(elem => {
          let output = elem.connectedOutput;
          output
        });
      }
    }
  })
;
