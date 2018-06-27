<template>
  <div class="spiner-container">
    <div class="spiner"></div>
  </div>
</template>

<script>
  export default {}
</script>

<style>

  .spiner-container {
    right: 0;
    position: absolute
  }

  .spiner {
    width: 10px;
    height: 10px;
    border: 2px solid lightgray;
    animation-name: Spin;
    animation-duration: 1.5s;
    animation-iteration-count: infinite;
    animation-timing-function: ease-in-out;
    /*--positions--*/
    transform-origin: center;
    top: 50%;
  }

  @keyframes Spin {
    0% {
      transform: rotate(0deg);
    }
    70% {
      transform: rotate(360deg);
    }
    100% {
      transform: rotate(360deg);
    }

  }
</style>
