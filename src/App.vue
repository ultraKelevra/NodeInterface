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

  .small span {
    font-size: calc(8px + 1vmin);
  }

  .icon {
    width: calc(10px + 2vmin);
    height: calc(10px + 2vmin);
  }

  .small .icon,
  .small.icon{
    width: calc(8px + 1vmin);
    height: calc(8px + 1vmin);
  }

  .big .icon,
  .big.icon{
    width: calc(10px + 3vmin);
    height: calc(10px + 3vmin);
  }

</style>
