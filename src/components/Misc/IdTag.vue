<template>
  <span class="id-tag">
    [<slot></slot>]
  </span>
</template>

<script>
  export default {
    props: ['id']
  }
</script>

<style scoped>
  .id-tag {
    color: gray;
    font-size: 12px;
  }
</style>
