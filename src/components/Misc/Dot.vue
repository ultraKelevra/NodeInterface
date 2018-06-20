<template>
  <div class="dot"></div>
</template>

<script>
  export default {
    props: ['connected', 'type']
  }
</script>

<style>
  .dot {
    width: 8px;
    height: 8px;
    top: 50%;
    transform: translateY(-50%);
    display: block;
    position: absolute;
    background: transparent;
    border-radius: 50%;
    border: 3px skyblue solid;
    transition: .25s;
  }

  .connected .dot {
    width: 0;
    height: 0;
    border: 5px skyblue solid;
  }

  .node-input .dot {
    left: 5px;
  }

  .node-output .dot {
    right: 5px;
  }
</style>
