<template>
  <div id="app">
    <drag-box :nodeLabels="nodeLabels">
    </drag-box>
  </div>
</template>

<script>
  import DragBox from './components/DragDropInterface/DragBox';
  import NodePicker from './components/DragDropInterface/NodePicker';

  export default {
    data() {
      return {
        nodeInstances: [],
        nodeLabels: [
          {code: 'merge', label: 'Combinar'},
          {code: 'split', label: 'Separar'},
          {code: 'crosstable', label: 'Frecuencias'}
        ],
        nodesBlueprint: [
          {
            code: 'merge',
            blueprint: {
              label: 'Combinar',
              inputs: [{name: 'A'}, {name: 'B'}, {name: 'C'}],
              outputs: [{name: 'out'}],
            }
          },
          {
            code: 'split',
            blueprint: {
              label: 'Separar',
              inputs: [{name: 'A'}, {name: 'B'}, {name: 'C'}],
              outputs: [{name: 'out'}],
            }
          },
          {
            code: 'crosstable',
            blueprint: {
              label: 'Frecuencias',
              inputs: [{name: 'A'}, {name: 'B'}, {name: 'C'}],
              outputs: [{name: 'out'}],
            }
          }
        ],
      }
    },
    methods: {},
    components: {
      DragBox,
      NodePicker
    }
  }
</script>

<style language="scss">
  @import './Style/transitions.scss';
  @import './Style/vars.scss';

  body {
    font-family: Calibri;
    font-size: 20px;
    background-color: rgb(50, 50, 50);
    color: white;
  }

  * {
    margin: 0;
    padding: 0;
  }

  span {
    user-select: none;
  }

  .icon {
    width: 2vmin;
    height: 2vmin;
  }

</style>
