<template>
  <div id="app">
    <drag-box></drag-box>
  </div>
</template>

<script>
  import DragBox from './components/DragDropInterface/DragBox';
  import NodePicker from './components/DragDropInterface/NodePicker';

  export default {
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
