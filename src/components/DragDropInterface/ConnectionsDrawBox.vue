<template>
  <svg class="draw-box"
       height="500vh"
       width="500vh"
       viewBox="1000,1000"
       @click.stop="$emit('drop')">
    <cubic-bezier v-for="(connection,index) in connections"
                  :start="connection.output"
                  :end="connection.input"
                  fill="none"
                  stroke="skyblue"
                  strokeWidth="3"
                  :key="index">
    </cubic-bezier>
  </svg>
</template>

<script>
  import CubicBezier from './CubicBezier';

  export default {
    props: ['connections'],
    components: {
      CubicBezier
    }
  }
</script>

<style>
  .draw-box {
    /*position: absolute;*/
    /*top: 0;*/
    /*left: 0;*/
    width: 500vh;
    height: 500vh;
  }
</style>
