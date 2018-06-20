<template>
  <div>
    <label :for="id">{{ blueprint.label }}</label>
    <input type="text"
           :id="compId">
  </div>
</template>

<script>
  export default {
    props: ['blueprint', 'compId']
  }
</script>

<style>

</style>
