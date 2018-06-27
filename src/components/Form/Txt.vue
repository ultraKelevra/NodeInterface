<template>
  <div class="mono-field">
    <label :for="id">{{ elem.label }}</label>
    <input type="text"
           :id="id">
  </div>
</template>

<script>
  export default {
    props: ['elem', 'id']
  }
</script>

<style>
  input {
    border: none;
    border-radius: 3px;
    color: rgb(50, 50, 50);
    font-size: 15px;
    padding: 2px 5px;
    box-shadow: inset 1px 1px 2px rgba(0, 0, 0, .2);
  }
</style>
