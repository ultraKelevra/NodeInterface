<template>
  <svg class="draw-box" height="500vh" width="500vh" viewBox="1000,1000">
    <defs>
      <!--<pattern viewBox="0 0 100 100"-->
      <!--x="0" y="0" width="100" height="100"-->
      <!--patternUnits="userSpaceOnUse"-->
      <!--patternContentUnits="objectBoundingBox"-->
      <!--id="cross-fill">-->
      <!--<g stroke="rgb(75,75,75)" stroke-width="1">-->
      <!--<line x1="0" y1="0" x2="5" y2="5"></line>-->
      <!--<line x1="100" y1="100" x2="95" y2="95"></line>-->
      <!--<line x1="100" y1="0" x2="95" y2="5"></line>-->
      <!--<line x1="0" y1="100" x2="5" y2="95"></line>-->
      <!--</g>-->
      <!--<g stroke="rgb(40,40,40)" stroke-width="1">-->
      <!--<line x1="45" y1="50" x2="55" y2="50"></line>-->
      <!--<line x1="50" y1="45" x2="50" y2="55"></line>-->
      <!--</g>-->
      <!--</pattern>-->
    </defs>
    <!--<rect x="0" y="0" width="100%" height="100%" fill="url(#cross-fill)"></rect>-->
    <cubic-bezier v-for="connection in connections"
                  :start="connection.start"
                  :end="connection.end"
                  fill="none"
                  stroke="skyblue"
                  strokeWidth="3">
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
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }
</style>
