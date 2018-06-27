<template>
  <div class="mono-field">
    <label :for="id">{{ elem.label }}</label>
    <input type="number"
           :id="id">
  </div>
</template>

<script>
  export default {
    props: ['elem', 'id']
  }
</script>

<style>

</style>
