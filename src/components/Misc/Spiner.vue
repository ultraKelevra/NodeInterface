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
  }

  .spiner {
    width: 50px;
    height: 50px;
    border: none;
    border-top: 3px solid white;
    border-radius: 3px;
    animation-name: spin;
    animation-duration: 2s;
    animation-timing-function: ease-in-out;
  }

  @keyframes spin {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }

  }
</style>
