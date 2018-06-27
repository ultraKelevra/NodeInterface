export const actions = {
  createNode({commit}, blueprint) {
    commit('createNode', blueprint);
  },
  deleteNode({commit}, node) {
    commit('deleteNode', node);
  },
  connect({commit}, event) {
    commit('connect', event);
  },
  disconnect({commit}, input) {
    commit('disconnect', input);
  },
};
