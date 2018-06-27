<template>
  <div class="mono-field">
    <label :for="id">
      <transition name="left" appear>
        <spiner></spiner>
      </transition>
      {{ elem.label }}
    </label>
    <select :id="id">
      <template v-if="updated">
        <option v-for="option in options">
          {{ option }}
        </option>
      </template>
      <option v-else>---------</option>
    </select>
  </div>
</template>

<script>
  import Spiner from '../Misc/Spiner';

  export default {
    props: ['elem', 'id'],
    data() {
      return {
        updated: true,
        options: ['AAA', 'BBB', 'DDDD'],
      };
    },
    components: {
      Spiner
    },
    mounted(){
    }
  }
</script>

<style>
  select {
    border-radius: 3px;
    border: none;
    background: rgb(120, 120, 120);
    color: white;
    font-size: 15px;
    padding: 2px 5px;
    box-shadow: 0 2px 2px 0px rgba(0, 0, 0, 0.3);
    transition: all .2s;
  }

  option {
    border-radius: 3px;
    border: none;
    background: rgb(120, 120, 120);
    color: white;
    font-size: 15px;
    padding: 2px 5px;
  }

  select:hover {
    color: rgb(50, 50, 50);
    background: rgb(200, 200, 200);
  }
</style>
