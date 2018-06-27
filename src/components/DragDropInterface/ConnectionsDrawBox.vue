<template>
  <svg class="draw-box"
       width="100%"
       height="100%"
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

</style>
