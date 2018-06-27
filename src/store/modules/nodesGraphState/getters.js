export const getters = {
  nodes({nodes}) {
    return nodes;
  },
  nodeById({nodes}, id) {
    return nodes.find(elem => id === elem.id);
  },
  inputById({inputs}, id) {
    return inputs.find(input => id === input.id);
  },
  outputById({outputs}, id) {
    return outputs.find(output => id === output.id);
  }
};
